from scanner import TokenType, _match_number, _match_identifier, _match_symbol
from tree import TreeNode


class Token:
    def __init__(self, token_type: TokenType, value):
        self.type = token_type
        self.value = value


def is_operator(char: str) -> bool:
    return len(char) == 1 and char in "+-/*"


def _tree_node(text: str, pos: int) -> tuple[TreeNode|None, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text):
        return None, pos
    if "0" <= text[pos] <= "9":
        # A digit signals the start of a number
        value, pos = _match_number(text, pos)
        new_node = TreeNode(Token(TokenType.NUMBER, value))
    elif text[pos].isalpha():
        # An alphabetic character signals an identifier
        identifier, pos = _match_identifier(text, pos)
        new_node = TreeNode(Token(TokenType.IDENTIFIER, identifier))
    else:
        # In all other cases, it is a symbol
        symbol, pos = _match_symbol(text, pos)
        new_node = TreeNode(Token(TokenType.SYMBOL, symbol))
        if is_operator(symbol):
            new_node._left, pos = _tree_node(text, pos)
            new_node._right, pos = _tree_node(text, pos)
        if not is_operator(symbol) or new_node._right is None or new_node._left is None:
            return None, pos
    return new_node, pos


def generate_expression_tree(text: str) -> TreeNode|None:
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
                " " +infix_expression_tree(tree._right) + ")")
    return str(tree._item.value)