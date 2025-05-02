import string

"""
PURPOSE: This script simplifies alegebraic expressions containing indices

AUTHOR: Mr Adam James Brierley

DATE: 26th April 2025
"""

def main():

    expression = input("Provide expression: ")

    # Read the data from the algebraic expression
    index_list, var_list, coeff_list, op_list = expression_reader(expression)

    print(f"Index list: {index_list}")
    print(f"Variable list: {var_list}")
    print(f"Coefficient list: {coeff_list}")
    print(f"Operations list: {op_list}")

    # Simplify the algebraic expression
    simplifier(op_list, coeff_list, expression)


def expression_reader(expression):

    counter = 0
    index_list = []
    var_list = []
    coeff_list = []
    op_list = []

    for char in expression:

        counter += 1

        if char == "^":
            index_list.append(expression[counter])

        if char in string.ascii_letters:
            var_list.append(char)
            coeff_list.append(expression[counter-2])

        if char == "/" or char == "*":
            op_list.append(char)



    return index_list, var_list, coeff_list, op_list

def simplifier(op_list, coeff_list, expression):
    
    # Division operation(s)
    div_index = op_list.index("/")
    div_result = int(coeff_list[div_index]) / int((coeff_list[div_index+1]))


main()