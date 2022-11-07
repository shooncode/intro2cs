from math import sqrt

# 1. Basic Calculator
def calc_math_expression(num1, num2, operator):

    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "*":
        return (num1 * num2)
    elif operator == ":":
        if num2 != 0:
            return (num1 / num2)
    else:
        return None

def calc_math_expression_from_str(str_input):
    parameter = str_input.split()
    num1 = float(parameter[0])
    operator = parameter[1]
    num2 = float(parameter[2])

    return calc_math_expression(num1, num2, operator)


# 2. Largest and Smallest Numbers
def find_largest_and_smallest_numbers(num1 = 0.0, num2 = 0.0, num3 = 0.0):

    if num1 >= num2 and num1 >= num3 and num2 >= num3:
        return (num1, num3)
    elif num1 >= num2 and num3 >= num2 and num1 >= num3:
        return (num1, num2)
    elif num2 >= num1 and num2 >= num3 and num1 >= num3:
        return (num2, num3)
    elif num2 >= num1 and num2 >= num3 and num3 >= num1:
        return (num2, num1)
    elif num3 >= num1 and num3 >= num2 and num1 >= num2:
        return (num3, num2)
    elif num3 >= num1 and num3 >= num2 and num2 >= num1:
        return (num3, num1)

# 3. Quadratic Equation Solver

def quadratic_equation_solver(a, b, c):
    if a == 0:
        return (None, None)

    else:
        root = (b * b) - (4 * (a * c))
        if root < 0:
            return (None, None)
        elif root == 0:
            solution1 = (-b) / (2 * a)
            return (solution1, None)
        else:
            solution1 = ((-b) + sqrt(root)) / (2 * a)
            solution2 = ((-b) - sqrt(root)) / (2 * a)
            return (solution1, solution2)

def quadratic_equation_solver_from_user_input(str_input):
    parameter = str_input.split()
    a = float(parameter[0])
    b = float(parameter[1])
    c = float(parameter[2])

    return quadratic_equation_solver(a, b, c)

# 4. Temp Checker
def temp_checker(min_temp, temp_1, temp_2, temp_3):
    temp_list = [temp_1, temp_2, temp_3]
    days = 0

    for temp in temp_list:
        if temp > min_temp:
            days += 1

    if days >= 2:
        return True
    else:
        return False
