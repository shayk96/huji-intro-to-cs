########################################################################
# FILE : math_print.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex1 2020
# DESCRIPTION: A simple program that shows how math can be done in python
#########################################################################
import math


def golden_ratio():
    """
    This function calculates the golden ratio
    """
    print((math.sqrt(5) + 1) / 2)


def six_squared():
    """
    This function calculates the square of 6
    """
    print(6 ** 2)


def hypotenuse():
    """
    This function calculates the hypotenuse
    """
    print(math.sqrt(5 ** 2 + 12 ** 2))


def pi():
    """
    This function prints the value of Pi
    """
    print(math.pi)


def e():
    """
    This function prints the value of e
    """
    print(math.e)


def squares_area():
    """
    This function prints the square of the numbers 1 to 10
    """
    print(1 ** 2, 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2, 6 ** 2, 7 ** 2, 8 ** 2, 9 ** 2, 10 ** 2)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
