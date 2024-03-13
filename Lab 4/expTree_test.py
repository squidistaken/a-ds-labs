from expTree import *

expression = input("give an expression: ")
while len(expression) == 0 or expression[0] != "!":
    tokentree = generate_expression_tree(expression)
    if tokentree is None:
        print("this is not an infix expression")
    else:
        print("expression:", end=" ")
        print(infix_expression_tree(tokentree))
        if is_numerical_expression_tree(tokentree):
            print("the value of this expression is:", end=" ")
            print(evaluate_expression_tree(tokentree))
        else:
            print("this is not a numerical infix expression")
            tokentree = simplify(tokentree)
            print("simplified:", end=" ")
            print(infix_expression_tree(tokentree))
            derivative = simplify(differentiate(tokentree, "x"))
            print("derivative to x:", end=" ")
            print(infix_expression_tree(derivative))
    expression = input("\ngive an expression: ")
print("good bye")