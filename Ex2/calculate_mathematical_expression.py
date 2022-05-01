###################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex2 2020
# DESCRIPTION: A simple program that calculates arithmetic actions
###################################################################


def calculate_mathematical_expression(num_1, num_2, action):
    """
    The function takes 2 numbers and the arithmetic action
    between them, calculates and returns the result
    """
    if action == '+':
        return num_1 + num_2
    elif action == '-':
        return num_1 - num_2
    elif action == '*':
        return num_1 * num_2
    elif action == '/':
        if num_2 != 0:
            return num_1 / num_2
        else:
            return None
    else:
        return None


def calculate_from_string(request):
    """
    The function takes a basic math question written as
    as string and returns an answer
    """
    num_1, action, num_2 = request.split(" ")
    num_1 = float(num_1)
    num_2 = float(num_2)
    action = str(action)
    return calculate_mathematical_expression(num_1, num_2, action)





