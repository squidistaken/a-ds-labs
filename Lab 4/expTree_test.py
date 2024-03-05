from expTree import *

expression = input("give an expression: ")
while expression[0] != "!":
    tokentree = generate_expression_tree(expression)
    print(tokentree)
    infix_expression_tree(tokentree)
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
    expression = input("\ngive an expression: ")
print("good bye")
