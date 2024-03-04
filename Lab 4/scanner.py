"""
File:   scanner.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A scanner that transforms a string into a linked list of tokens
"""
from enum import Enum


class TokenType(Enum):
    """
    Tokens can be of three types:
    numbers (digits), identifiers (characters), and symbols (any)
    """
    NUMBER = 1
    IDENTIFIER = 2
    SYMBOL = 3


class TokenList:
    def __init__(self, value = None):
        self._type = TokenType.NUMBER
        self._value = value
        self._next = None

    def __str__(self):
        return_value = str(self._value)
        if self._next is not None:
            return_value += " " + str(self._next)
        return return_value


def _match_number(input_str: str, position: int) -> tuple[int, int]:
    # Precondition: input_str[position] is a number
    number = ""
    # Maybe accept a "-"?
    while position < len(input_str) and "0" <= input_str[position] <= "9":
        number += input_str[position]
        position += 1
    return int(number), position


def _match_identifier(input_str: str, position: int) -> tuple[str, int]:
    # Precondition: input_str[position] is a letter
    old_position = position
    while position < len(input_str) and input_str[position].isalnum():
        position += 1
    return input_str[old_position:position], position


def _match_symbol(input_str: str, position: int) -> tuple[str, int]:
    return input_str[position], position+1


def _generate_node(input_str: str, position: int) -> tuple[TokenList, int]:
    # Precondition: input_str is not whitespace
    new_node = TokenList()
    if "0" <= input_str[position] <= "9":
        new_node._type = TokenType.NUMBER
        new_node._value, position = _match_number(input_str, position)
    elif input_str[position].isalpha():
        new_node._type = TokenType.IDENTIFIER
        new_node._value, position = _match_identifier(input_str, position)
    else:
        new_node._type = TokenType.SYMBOL
        new_node._value, position = _match_symbol(input_str, position)
    return new_node, position


def generate_token_list(input_str: str) -> TokenList:
    front = None
    back = None
    position = 0
    while position < len(input_str):
        if input_str[position].isspace():
            position += 1
        else:
            new_node, position = _generate_node(input_str, position)
            if front is None:
                front = new_node
                back = new_node
            else:
                back._next = new_node
                back = new_node
    return front

