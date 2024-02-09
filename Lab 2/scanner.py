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
    def __init__(self):
        self._type = TokenType.NUMBER
        self._value = None
        self._next = None

    def __str__(self):
        return_value = str(self._value)
        if self._next is not None:
            return_value += " " + str(self._next)
        return return_value


def _match_number(text: str, position: int) -> tuple[int, int]:
    """
    Reads a number from the input
    :param text: input string
    :param position: start position of the number
    :return: (number read, first position in text after the read number)
    """
    output = 0
    while position < len(text) and "0" <= text[position] <= "9":
        output = output*10 + int(text[position])
        position += 1
    return output, position


def _match_symbol(text: str, position: int) -> tuple[str, int]:
    """
    Reads a single character as a symbol from the input
    :param text: input string
    :param position: start position of the symbol
    :return: (symbol read, first position in text after the read symbol)
    """
    return text[position], position + 1


def _match_identifier(text: str, position: int) -> tuple[str, int]:
    """
    Reads an identifier  from the input
    :param text: input string
    :param position: start position of the identifier
    :return: (identifier read, first position in text after the read identifier)
    """
    old_position = position
    while position < len(text) and text[position].isalnum():
        position += 1
    return text[old_position:position], position


def _generate_node(text: str, position: int) -> tuple[TokenList, int]:
    """
    Generates a new TokenList node.
    :param text: string to read the node information from
    :param position: start position of the information
    :return: a tuple with the generated node and the new position in the input
    """
    new_node = TokenList()
    if "0" <= text[position] <= "9":
        # A digit signals the start of a number
        new_node._type = TokenType.NUMBER
        new_node._value, position = _match_number(text, position)
    elif text[position].isalpha():
        # An alphabetic character signals an identifier
        new_node._type = TokenType.IDENTIFIER
        new_node._value, position = _match_identifier(text, position)
    else:
        # In all other cases, it is a symbol
        new_node._type = TokenType.SYMBOL
        new_node._value, position = _match_symbol(text, position)
    return new_node, position


def generate_token_list(text: str) -> TokenList:
    head = None
    tail = None
    position = 0
    while position < len(text):
        if text[position].isspace():
            position += 1
        else:
            node, position = _generate_node(text, position)
            if head is None:
                head = node
            else:
                tail._next = node
            tail = node
    return head




