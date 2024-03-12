from expTree import *

expression = input("give an expression: ")
while expression[0] != "!":
    tokentree = generate_expression_tree(expression)
    if tokentree is None:
        print("this is not an infix expression")
    else:
        print("expression:", end=" ")
        print(infix_expression_tree(tokentree))

        tree = simplify(tokentree)
        print("simplified expression:", end=" ")
        print(infix_expression_tree(tree))

        if is_numerical_expression_tree(tokentree):
            print("the value of this expression is:", end=" ")
            print(evaluate_expression_tree(tokentree))
        else:
            print("this is not a numerical infix expression")
            tree = simplify(differentiate(tree))
            print("differentiated expression:", end=" ")
            print(infix_expression_tree(tree))
    expression = input("\ngive an expression: ")
print("good bye")
