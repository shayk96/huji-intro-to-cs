###################################################################
# FILE : shapes.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex2 2020
# DESCRIPTION: A simple program that calculates the areas of shapes
###################################################################
import math


def circle_area(r):
    """
    This function calculates and returns the area of a circle
    """
    return pow(r, 2) * math.pi


def rectangle_area(a, b):
    """
    This function calculates and returns the area of a rectangle
    """
    return a * b


def triangle_area(a):
    """
    This function calculates and returns the area of a triangle
    """
    return pow(a, 2) * (math.sqrt(3) / 4)


def shape_area():
    """
    This function gets the choice of shape and values of the
     variables from the user and returns the area of the shape
    """
    shape = str(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape == str(1):
        r = float(input())
        return circle_area(r)
    elif shape == str(2):
        a = float(input())
        b = float(input())
        return rectangle_area(a, b)
    elif shape == str(3):
        a = float(input())
        return triangle_area(a)
    else:
        return None

