from recognizeEq import *
from evalEq import *

expression = input("give an equation: ")
while expression == "" or expression[0] != "!":
    tokenlist = generate_token_list(expression)
    if recognize_equation(tokenlist):
        if not is_single_variable_equation(tokenlist):
            print("this is an equation, but not in 1 variable")
        else:
            degree = get_degree(tokenlist)
            print("this is an equation in 1 variable of degree", degree)
            if degree == 1:
                print("solution:", evaluate_equation(tokenlist))
    else:
        print("this is not an equation")
    expression = input("\ngive an equation:")
print("good bye")
