"""
File: recognizeEq.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)
Contributors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A recognizer that determines whether a given token list represents a valid equation.
    Modified by Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl).
"""
from scanner import *


class TokenListPosition:
    def __init__(self, tokens: TokenList):
        self.tokens = tokens


def _accept_number(position: TokenListPosition) -> bool:
    """
    Reads a number off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff a number has been read off the token list
    """
    if position.tokens is not None and position.tokens._type == TokenType.NUMBER:
        position.tokens = position.tokens._next
        return True
    return False


def _accept_identifier(position: TokenListPosition) -> bool:
    """
    Reads an identifier off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff an identifier has been read off the token list
    """
    if position.tokens is not None and position.tokens._type == TokenType.IDENTIFIER:
        position.tokens = position.tokens._next
        return True
    return False


def _accept_symbol(position: TokenListPosition, symbol: str) -> bool:
    """
    Reads a symbol off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff a symbol has been read off the token list
    """
    if position.tokens is not None and position.tokens._type == TokenType.SYMBOL and position.tokens._value == symbol:
        position.tokens = position.tokens._next
        return True
    return False


def _accept_exponent(position: TokenListPosition) -> bool:
    """
    Reads an exponent off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff an exponent has been read off the token list
    """
    return _accept_number(position)


def _accept_term(position: TokenListPosition) -> bool:
    """
    Reads a maximal term off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff a term has been read off the token list
    """
    # <term> ::= <nat> | [<nat>] <identifier> ['^' <nat>]

    # <nat>
    if _accept_number(position):
        if _accept_identifier(position):
            if _accept_symbol(position, "^"):
                return _accept_number(position)
            return True
        return True
    # <identifier> ['^' <nat>]
    if _accept_identifier(position):
        if _accept_identifier(position):
            return False
        if _accept_symbol(position, "^"):
            if not _accept_number(position):
                return False
        return True


def _accept_expression(position: TokenListPosition) -> bool:
    """
    Reads a maximal expression off the token list, if it exists
    :param position: pointer to a token list node
    :return: True iff an expression has been read off the token list
    """
    # <expression> :== ['-'] <term> {'+' <term> | '-' <term>}

    # ['-'] <term>
    if _accept_symbol(position, "-"):
        if not _accept_term(position):
            return False
        # {'+' <term> | '-' <term>}
        while _accept_symbol(position, "+") or _accept_symbol(position, "-"):
            if not _accept_term(position):
                return False
        return True
    # <term>
    else:
        if not _accept_term(position):
            return False
        # {'+' <term> | '-' <term>}
        while _accept_symbol(position, "+") or _accept_symbol(position, "-"):
            if not _accept_term(position):
                return False
        return True


def _accept_equation(position: TokenListPosition) -> bool:
    # <equation> ::= <expression> '=' <expression>
    if not _accept_expression(position):
        return False
    if not _accept_symbol(position, "="):
        return False
    if not _accept_expression(position):
        return False
    return True


def recognize_equation(tokenlist: TokenList) -> bool:
    """
    Determines whether the given token list represents a valid equation
    :param tokenlist: input token list
    :return: True iff the token list represents a valid equation
    """
    position = TokenListPosition(tokenlist)
    return _accept_equation(position) and position.tokens is None


def get_degree(tokenlist: TokenList) -> int:
    """
    Determines the highest exponent in a token list
    :param tokenlist: input token list
    :return: the highest exponent in the token list
    """
    position = TokenListPosition(tokenlist)
    total = 1

    while position.tokens is not None:
        if _accept_symbol(position, "^"):
            new_exponent = position.tokens._value
            total = max(new_exponent, total)
        else:
            position.tokens = position.tokens._next

    return total


def is_single_variable_equation(tokenlist: TokenList) -> bool:
    """
    Determines whether a token list contains exactly one identifier
    :param tokenlist: input token list
    :return: True iff the token list contains exactly one identifier
    """
    position = TokenListPosition(tokenlist)
    identifiers = []

    while position.tokens is not None:
        if position.tokens._type == TokenType.IDENTIFIER:
            if position.tokens._value not in identifiers:
                identifiers.append(position.tokens._value)
        position.tokens = position.tokens._next

    return len(identifiers) == 1
