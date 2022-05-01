###################################################################
# FILE : largest_and_amallest.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex2 2020
# DESCRIPTION: A simple program that checks which number is the largest
# and which one is the smallest
# i chose (1,1,0) and (30,30,30) to check edge cases
###################################################################


def largest_and_smallest(num_1, num_2, num_3):
    """
    This function takes 3 numbers and checks the max and min values
    """
    if num_1 >= num_2:
        a = num_1
        b = num_2
    else:
        a = num_2
        b = num_1
    if b > num_3:
        return a, num_3
    else:
        if a > num_3:
            return a, b
        else:
            return num_3, b


def check_largest_and_smallest():
    """
    This function checks if the function "largest_and_smallest" works correctly
    """
    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    elif largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    elif largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    elif largest_and_smallest(1, 1, 0) != (1, 0):
        return False
    elif largest_and_smallest(30, 30, 30) != (30, 30):
        return False
    else:
        return True