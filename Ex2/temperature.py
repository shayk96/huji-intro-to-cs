###################################################################
# FILE : temperature.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex2 2020
# DESCRIPTION: A simple program that checks is it summer yet
###################################################################


def is_it_summer_yet(a, b, c, d):
    """
    This function checks if at least 2 of the last 3 parameters
     are higher than the first one and returns True or False
    """
    if d > a:
        if c > a or b > a:
            return True
        else:
            return False
    elif b > a and c > a:
        return True
    else:
        return False
