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
from recognizeEq import _accept_symbol


class TokenListEvaluation:
    def __init__(self, tokens: TokenList):
        self.tokens = tokens
        self.value = 0


def _value_number(status: TokenListEvaluation) -> bool:
    """
    Records the value of a number, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff a number has been read off the token list
    """
    if status.tokens is not None and status.tokens._type == TokenType.NUMBER:
        status.value = status.tokens._value
        status.tokens = status.tokens._next
        return True
    return False


def _value_factor(status: TokenListEvaluation) -> bool:
    """
    Records the value of a factor, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff a factor has been read off the token list
    """
    return _value_number(status) or \
        (_accept_symbol(status, "(") and  _value_expression(status) and _accept_symbol(status, "("))


def _value_term(status: TokenListEvaluation) -> bool:
    """
    Records the value of a maximal term, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff a term has been read off the token list
    """
    if not _value_factor(status):
        # A term must start with a factor
        return False
    value = status.value
    while status.tokens is not None:
        if _accept_symbol(status, "*"):
            if _value_factor(status):
                value *= status.value
            else:
                return False
        elif _accept_symbol(status, "/"):
            if _value_factor(status):
                value /= status.value
            else:
                return False
        else:
            status.value = value
            return True
    # If there are no more * or /, the term is finished
    status.value = value
    return True


def _value_expression(status: TokenListEvaluation) -> bool:
    """
    Records the value of a maximal expression, if it exists
    :param position: pointer to a token list node evaluation
    :return: True iff an expression has been read off the token list
    """
    if not _value_term(status):
        # An expression must start with a term
        return False
    value = status.value
    while status.tokens is not None:
        if _accept_symbol(status, "+"):
            if _value_term(status):
                value += status.value
            else:
                return False
        elif _accept_symbol(status, "-"):
            if _value_term(status):
                value -= status.value
            else:
                return False
        else:
            status.value = value
            return True
    # If there are no more + or -, the expression is finished
    status.value = value
    return True


def evaluate_equation(tokenlist: TokenList):
    """
    Determines whether a given token list represents a valid numerical expression
    and return the value if it is
    :param tokenlist: token list
    :return: the value of the expression represented by tokenlist,
    or None if tokenlist is not a valid expression
    """
    status = TokenListEvaluation(tokenlist)
    if _value_expression(status) and status.tokens is None:
        return status.value
    return None


