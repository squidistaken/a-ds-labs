from scanner import TokenType, _match_number, _match_identifier, _match_symbol
from tree import TreeNode


class Token:
    def __init__(self, token_type: TokenType, value):
        self.type = token_type
        self.value = value


def is_operator(char: str) -> bool:
    return len(char) == 1 and char in "+-/*"


def _tree_node(text: str, pos: int) -> tuple[TreeNode | None, int]:
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


def _find_main_operator(expr):
    # Crucial for finding the smallest precedence. float('inf') ensures it is bigger than any given val
    min_precedence = float('inf')
    main_operator = -1
    stack = []
    for i, char in enumerate(expr):
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        elif not stack and is_operator(char) and _precedence(char) <= min_precedence:
            min_precedence = _precedence(char)
            main_operator = i
    return main_operator


def _precedence(operator):
    """
    returns whether the operator is either multiplication and division or addition and subtraction
    :param operator:
    :return:
    """
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    return 0


def convert(expr):
    """
    Converts a part of the expression to prefix recursively.
    """
    # Base case: If the expression is a single operand or empty
    if not expr or expr.isdigit() or (len(expr) == 1 and expr.isalpha()):
        return expr

    # Split expression by the main operator
    index = _find_main_operator(expr)
    if index == -1:
        return expr  # No operator found, return as is

    # Recursive calls
    before = expr[:index]
    after = expr[index + 1:]
    operator = expr[index]

    # Process before and after recursively
    left = convert(before)
    right = convert(after)

    # Combine results
    return operator + left + right


def _infix_to_prefix(expr):
    """
    Takes in an infix expression and converts it into a prefix string.
    :return: prefix variant of input equation
    """
    # Handle parentheses first by finding the most outer pair and processing its content
    while '(' in expr:
        start = end = expr.find('(')
        while end < len(expr) and expr[end] != ')':
            if expr[end] == '(':
                start = end
            end += 1
        # Process the content within the outermost parentheses
        inner_prefix = convert(expr[start + 1:end])
        expr = expr[:start] + inner_prefix + expr[end + 1:]

    return convert(expr)


def generate_expression_tree(text: str) -> TreeNode | None:
    tree, position = _tree_node(text, 0)
    print(f"tree: {tree}\nposition: {position}")
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
