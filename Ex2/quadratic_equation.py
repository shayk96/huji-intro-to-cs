###################################################################
# FILE : quadratic_equation.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex2 2020
# DESCRIPTION: A simple program that does quadratic equations
###################################################################
import math


def discriminant(a, b, c):
    """
    This function calculates and returns
    the discriminant part of the equation
    """
    return pow(b, 2) - (4 * a * c)


def calculate(a, b, c):
    """
    This function calculates and returns
    the 2 solutions of the equation
    """
    return ((-b) + math.sqrt(discriminant(a, b, c))) / (2 * a), \
           ((-b) - math.sqrt(discriminant(a, b, c))) / (2 * a)


def quadratic_equation(a, b, c):
    """
    This function calculates and returns
    the solution using the two prior functions
    """
    if discriminant(a, b, c) < 0:
        return None, None
    elif discriminant(a, b, c) == 0:
        return (-b) / (2 * a), None
    else:
        return calculate(a, b, c)


def quadratic_equation_user_input():
    """
    This function gets its variables from the user, calculates
    and prints the solutions of the quadratic equation
    """
    coefficients = input("Insert coefficients a, b, and c: ")
    a, b, c = coefficients.split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        x, y = quadratic_equation(a, b, c)
        if x == y == None:
            print('The equation has no solutions')
        else:
            if y == None:
                print('The equation has 1 solution:', x)
            else:
                print('The equation has 2 solutions:', x, 'and', y)