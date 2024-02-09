"""
File:   recognizeEq.py
Author: Harmen de Weerd (harmen.de.weerd@rug.nl)

Description:
    A recognizer that determines whether a given token list
    represents a valid equation
"""
from scanner import *


def recognize_equation(tokenlist: TokenList) -> bool:
    """
    Determines whether the given token list represents a valid equation
    :param tokenlist: input token list
    :return: True iff the token list represents a valid equation
    """
    return False


def get_degree(tokenlist: TokenList) -> int:
    """
    Determines the highest exponent in a token list
    :param tokenlist: input token list
    :return: the highest exponent in the token list
    """
    return -1


def is_single_variable_equation(tokenlist: TokenList) -> bool:
    """
    Determines whether a token list contains exactly one identifir
    :param tokenlist: input token list
    :return: True iff the token list contains exactly one identifier
    """
    return False




