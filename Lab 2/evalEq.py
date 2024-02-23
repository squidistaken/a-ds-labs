"""
File: evalEq.py
Authors:
    Marcus Harald Olof Persson (m.h.o.persson@student.rug.nl)
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    An evaluator that determines the value of a given token list
    if it represents a valid equation
"""
from scanner import *
from recognizeEq import _accept_symbol, _accept_identifier


class TokenListEvaluation:
    def __init__(self, tokens: TokenList):
        self.tokens = tokens
        # Temporary value to store values
        self.temp = 0
        # Values we are computing in the end
        self.natural = 0
        self.identifier = 0
        self.equation_value = 0
        # Booleans to check progress
        self.is_natural = False
        self.switch_operations = False


def _value_number(status: TokenListEvaluation) -> bool:
    """
    Records the value of a number, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff a number has been read off the token list
    """
    if status.tokens is not None and status.tokens._type == TokenType.NUMBER:
        status.temp = status.tokens._value
        status.tokens = status.tokens._next
        return True
    return False


def _value_term(status: TokenListEvaluation) -> bool:
    """
    Records the value of a maximal term, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff a term has been read off the token list
    """
    # <term> ::= <nat> | [<nat>] <identifier> ['^' <nat>]

    if _value_number(status):
        if not _accept_identifier(status):
            status.is_natural = True
        else:
            status.is_natural = False
    if _accept_identifier(status):
        status.temp = 1
        status.is_natural = False

    # Account if there is just an "x"
    value = status.temp

    while status.tokens is not None:
        if _accept_symbol(status, "^"):
            if _value_number(status):
                if status.temp != 0:
                    value **= status.temp
            else:
                return False
        else:
            status.temp = value
            return True
    # If there are no more * or /, the term is finished
    status.temp = value
    return True


def _value_expression(status: TokenListEvaluation) -> bool:
    """
    Records the value of a maximal expression, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff an expression has been read off the token list
    """
    # <expression> :== ['-'] <term> {'+' <term> | '-' <term>}

    # [-] <term>
    if _accept_symbol(status, "-"):
        if not _value_term(status):
            return False
        else:
            status.temp = -status.temp
    if _value_term(status):
        status.temp = status.temp

    if status.is_natural:
        status.natural += status.temp if not status.switch_operations else - status.temp
    else:
        status.identifier += status.temp if not status.switch_operations else - status.temp

    while status.tokens is not None:
        if _accept_symbol(status, "+"):
            if _value_term(status):
                if status.is_natural:
                    status.natural += status.temp if not status.switch_operations else - status.temp
                else:
                    status.identifier += status.temp if not status.switch_operations else - status.temp
            else:
                return False
        elif _accept_symbol(status, "-"):
            if _value_term(status):
                if status.is_natural:
                    status.natural -= status.temp if not status.switch_operations else + status.temp
                else:
                    status.identifier -= status.temp if not status.switch_operations else + status.temp
            else:
                return False
        else:
            status.temp = 0
            return True
    # If there are no more + or -, the expression is finished
    status.temp = 0
    return True


def _value_equation(status: TokenListEvaluation) -> bool:
    """
    Records the value of the equation, if it it exists
    :param position: pointer to a token list node evaluation
    :return: True iff an expression has been read off the token list
    """
    # <equation> ::= <expression> '=' <expression>

    if not _value_expression(status):
        return False
    if not _accept_symbol(status, "="):
        return False
    status.switch_operations = True
    if not _value_expression(status):
        return False
    if status.identifier == 0:
        return False
    status.equation_value = -status.natural / status.identifier
    return True


def evaluate_equation(tokenlist: TokenList):
    """
    Determines whether a given token list represents a valid numerical equation
    and return the value if it is
    :param tokenlist: token list
    :return: the value of the expression represented by tokenlist,
    or None if tokenlist is not a valid expression
    """
    status = TokenListEvaluation(tokenlist)
    if _value_equation(status) and status.tokens is None:
        return f"solution: {'%.3f' % status.equation_value}"
    return "not solvable"
