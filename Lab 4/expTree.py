"""
File: expTree.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A modified expression tree, fit to solve infix AND prefix expressions.
"""

from scanner import TokenType, _match_number, _match_identifier, _match_symbol
from tree import TreeNode


class Token:
    def __init__(self, token_type: TokenType, value):
        self.type = token_type
        self.value = value


def is_operator(char: str) -> bool:
    return len(char) == 1 and char in "+-/*"


def _create_subtree(operators: list, nodes: list):
    """
    Creates a subtree and stores in the nodes list.
    :param operators: Operators list.
    :param nodes: Nodes list.
    :return:
    """
    new_node = operators.pop()
    new_node._right = nodes.pop()
    new_node._left = nodes.pop()
    nodes.append(new_node)


def _tree_node(text: str, pos: int) -> tuple[TreeNode | None, int]:
    """
    Creates a tree.
    :param text: Given string.
    :param pos: Current position.
    :return:
    """
    operators = []
    nodes = []

    prev = None

    while pos < len(text):
        if pos < len(text) and text[pos].isspace():
            pos += 1
        elif "0" <= text[pos] <= "9":
            if prev != TokenType.SYMBOL and prev is not None:
                return None, pos
            # A digit signals the start of a number
            value, pos = _match_number(text, pos)
            new_node = TreeNode(Token(TokenType.NUMBER, value))
            nodes.append(new_node)
            prev = TokenType.NUMBER
        elif text[pos].isalpha():
            if prev != TokenType.SYMBOL and prev is not None:
                return None, pos
            # An alphabetic character signals an identifier
            identifier, pos = _match_identifier(text, pos)
            new_node = TreeNode(Token(TokenType.IDENTIFIER, identifier))
            nodes.append(new_node)
            prev = TokenType.IDENTIFIER
        else:
            # In all other cases, it is a symbol
            prev = TokenType.SYMBOL
            symbol, pos = _match_symbol(text, pos)
            if symbol not in "*/+-()":
                return None, pos
            root_node = TreeNode(Token(TokenType.SYMBOL, symbol))

            if len(operators) == 0:
                operators.append(root_node)
            elif symbol == "(":
                operators.append(root_node)
            elif symbol in "+-":
                while len(operators) and operators[-1]._item.value in "*/+-":
                    if len(nodes) == 0 or len(nodes) == 1:
                        return None, pos
                    _create_subtree(operators, nodes)
                    if len(operators) == 0:
                        break
                operators.append(root_node)
            elif symbol in "*/":
                while len(operators) and operators[-1]._item.value in "*/":
                    if len(nodes) == 0 or len(nodes) == 1:
                        return None, pos
                    _create_subtree(operators, nodes)
                    if len(operators) == 0:
                        break
                operators.append(root_node)
            elif symbol == ")":
                while len(operators) and operators[-1]._item.value != "(":
                    if len(nodes) == 0 or len(nodes) == 1:
                        return None, pos
                    _create_subtree(operators, nodes)
                    if len(operators) == 0:
                        break
                if not len(operators):
                    return None, pos
                operators.pop()

    while len(operators) != 0:
        new_node = operators.pop()
        if len(nodes) == 0 or len(nodes) == 1:
            return None, pos
        new_node._right = nodes.pop()
        new_node._left = nodes.pop()
        nodes.append(new_node)

    return nodes[-1], pos


def generate_expression_tree(text: str) -> TreeNode | None:
    if text == "":
        return None
    if is_operator(text[0]):
        return None
    if text in "()":
        return None
    tree, position = _tree_node(text, 0)
    if position == len(text):
        return tree
    return None


def is_numerical_expression_tree(tree: TreeNode) -> bool:
    if tree is None or tree._item.type == TokenType.IDENTIFIER:
        return False
    if tree._item.type == TokenType.NUMBER:
        return True
    return is_numerical_expression_tree(tree._left) and is_numerical_expression_tree(tree._right)


def evaluate_expression_tree(tree: TreeNode) -> float:
    if tree._item.type == TokenType.NUMBER:
        return tree._item.value
    left_operand = evaluate_expression_tree(tree._left)
    right_operand = evaluate_expression_tree(tree._right)
    match tree._item.value:
        case "*":
            return left_operand * right_operand
        case "/":
            return left_operand / right_operand
        case "-":
            return left_operand - right_operand
        case _:
            return left_operand + right_operand


def infix_expression_tree(tree: TreeNode) -> str:
    if tree is None:
        return "!"
    if tree._item.type == TokenType.SYMBOL:
        return ("(" + infix_expression_tree(tree._left) +
                " " + tree._item.value +
                " " + infix_expression_tree(tree._right) + ")")
    return str(tree._item.value)
