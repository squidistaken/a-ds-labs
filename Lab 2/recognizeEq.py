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

def recognize_equation(tokenlist: TokenList) -> bool:
    """
    Determines whether the given token list represents a valid equation
    :param tokenlist: input token list
    :return: True iff the token list represents a valid equation
    """
    equation = tokenlist.__str__()

    if "(" in equation or ")" in equation:
        return False
    if equation.find("=") == 0 or equation.find("=") == len(equation) - 1:
        return False
    if equation.count("=") == 1:
        return True
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
    Determines whether a token list contains exactly one identifier
    :param tokenlist: input token list
    :return: True iff the token list contains exactly one identifier
    """
    return False
