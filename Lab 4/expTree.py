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
    :return: Tuple of the final tree and last indexed position.
    """
    operators = []
    nodes = []

    prev = None

    while pos < len(text):
        # Increment position if there is a space character AND we are not reaching the end of the text.
        if pos < len(text) and text[pos].isspace():
            pos += 1
        # If there is a number.
        elif "0" <= text[pos] <= "9":
            if prev != TokenType.SYMBOL and prev is not None:
                return None, pos
            # A digit signals the start of a number
            value, pos = _match_number(text, pos)
            new_node = TreeNode(Token(TokenType.NUMBER, value))
            nodes.append(new_node)
            prev = TokenType.NUMBER
        # If there is an alphabetical character - an identifier.
        elif text[pos].isalpha():
            if prev != TokenType.SYMBOL and prev is not None:
                return None, pos
            identifier, pos = _match_identifier(text, pos)
            new_node = TreeNode(Token(TokenType.IDENTIFIER, identifier))
            nodes.append(new_node)
            prev = TokenType.IDENTIFIER
        else:
            # In all other cases, it is a symbol
            prev = TokenType.SYMBOL
            symbol, pos = _match_symbol(text, pos)
            # Validate for correct symbols.
            if symbol not in "*/+-()":
                return None, pos
            root_node = TreeNode(Token(TokenType.SYMBOL, symbol))

            # If we encounter our first operator, we shouldn't need to do much.
            if len(operators) == 0:
                operators.append(root_node)
            # Opening bracket
            elif symbol == "(":
                operators.append(root_node)
            # +-
            elif symbol in "+-":
                while len(operators) and operators[-1]._item.value in "*/+-":
                    if len(nodes) == 0 or len(nodes) == 1:
                        return None, pos
                    _create_subtree(operators, nodes)
                    if len(operators) == 0:
                        break
                operators.append(root_node)
            # */
            elif symbol in "*/":
                while len(operators) and operators[-1]._item.value in "*/":
                    if len(nodes) == 0 or len(nodes) == 1:
                        return None, pos
                    _create_subtree(operators, nodes)
                    if len(operators) == 0:
                        break
                operators.append(root_node)
            # Closing bracket.
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

    # Final validation in constructing the tree.
    while len(operators) != 0:
        new_node = operators.pop()
        if len(nodes) == 0 or len(nodes) == 1:
            return None, pos
        new_node._right = nodes.pop()
        new_node._left = nodes.pop()
        nodes.append(new_node)

    return nodes[-1], pos


def generate_expression_tree(text: str) -> TreeNode | None:
    """
    Generates an expression tree.
    :param text: Text.
    :return: Expression tree represented as a TreeNode.
    """
    if text == "":
        return None
    if is_operator(text[0]):
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


# Part 2
# Question 1

def simplify_expression_tree(tree: TreeNode) -> TreeNode:
    def simplify_node(node: TreeNode) -> [TreeNode, bool]:
        """
        Simplify expression
        (0 ∗ E) and (E ∗ 0) are simplified to 0;
        (0 + E), (E + 0), (E − 0), (1 ∗ E), (E ∗ 1) and (E / 1) are simplified to E.
        :param node: expression tree you want to simplify
        :return: simplified expression tree
        """

        # Base case: if the node is not a symbol return the current node
        if node._item.type != TokenType.SYMBOL:
            return node, False

        # Need to check whether anything changed in the tree.
        changed = False
        node._left, left_changed = simplify_node(node._left)
        node._right, right_changed = simplify_node(node._right)
        changed = left_changed or right_changed

        if node._item.value == "*":
            # If either of the children are 0 replace node with 0
            if node._left._item.value == 0 or node._right._item.value == 0:
                return TreeNode(Token(TokenType.NUMBER, 0)), True

            # If either of the children are 1 replace node with the other child
            if node._left._item.value == 1:
                return node._right, True
            # Vice versa for the right node
            elif node._right._item.value == 1:
                return node._left, True
        elif node._item.value == "+":
            # If the left node is 0 and adds another number or identifier replace node with right child
            if node._left._item.value == 0:
                return node._right, True
            # Vice versa for the right node
            if node._right._item.value == 0:
                return node._left, True
        elif node._item.value == "/":
            # Division by 1: replace node with left child
            if node._right._item.value == 1:
                return node._left, True
        elif node._item.value == "-":
            # Subtraction of 0: replace node with left child
            if node._right._item.value == 0:
                return node._left, True

        # return node if nothing changed.
        return node, changed

    simplified, changed = simplify_node(tree)
    # While there has been a change in the tree; simplify again till no simplifications are left
    while changed:
        simplified, changed = simplify_node(simplified)

    return simplified
