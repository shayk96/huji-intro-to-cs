#################################################################
# FILE : ex7.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex7 2020
# DESCRIPTION: a little program that does a lot of recursions
#################################################################


def print_to_n(n):
    """
    gets a number and prints all the numbers up to it
    :param n: an integer
    :return: prints the numbers
    """
    if n >= 1:
        print_to_n(n - 1)
        print(n)


def digit_sum(n):
    """
    takes a number and returns the sum of the digits of the number
    :param n: an integer
    :return: the sum of the digits of the number
    """
    if n < 10:
        return n
    else:
        last_digit = n % 10
        left_over = n // 10
        return last_digit + digit_sum(left_over)


def is_prime(n):
    """
    checks if the number n is a prime number
    :param n: an integer
    :return: True if the number is a prime, else False
    """
    if n <= 1:
        return False
    else:
        return has_divisor_smaller_than(n, 2)


def has_divisor_smaller_than(n, i):
    """
    gets a number and checks if it has divisors
    :param n: the number to check for dividers
    :param i: the divider
    :return: True if the number does not have dividers, else False
    """
    if i > n ** 0.5:
        return True
    if n % i == 0:
        return False
    if has_divisor_smaller_than(n, i + 1):
        return True
    else:
        return False


def play_hanoi(hanoi, n, src, dst, temp):
    """
    solves the hanoi game
    :param hanoi: the game
    :param n: number of disks
    :param src: the start pole
    :param dst: the end pole
    :param temp: the extra pole
    :return: None
    """
    if n >= 1:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        make_move(hanoi, src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def make_move(hanoi, src, dst):
    """
    moves the disks from one pole to another
    :param hanoi: the game
    :param src: pole to move disk from
    :param dst: pole to move disk to
    :return: None
    """
    hanoi.move(src, dst)


def print_sequences(char_list, n):
    """
    receives a list of characters and prints all the possible combination in
    the length of n
    :param char_list: a list of characters
    :param n: the length of the combinations
    :return: None
    """
    sequences_helper(char_list, n)


def sequences_helper(char_list, n, res=''):
    """
    receives a list of characters and prints all the possible combination in
    the length of n
    :param char_list: a list of characters
    :param n: the length of the combinations
    :param res: holds the combination
    :return: prints the combinations
    """
    if n == 0:
        print(res)
        return
    for idx in range(len(char_list)):
        temp = res + char_list[idx]
        sequences_helper(char_list, n - 1, temp)


def print_no_repetition_sequences(char_list, n):
    """
    receives a list of characters and prints all the possible combination in
    the length of n without repetitions of characters
    :param char_list: a list of characters
    :param n: the length of the combinations
    :return: None
    """
    no_repetition_sequences_helper(char_list, n)


def no_repetition_sequences_helper(char_list, n, res=''):
    """
    receives a list of characters and prints all the possible combination in
    the length of n without repetitions of characters
    :param char_list: a list of characters
    :param n: the length of the combinations
    :param res: holds the combination
    :return: prints the combinations
    """
    if n == 0:
        print(res)
        return
    for idx in range(len(char_list)):
        if char_list[idx] in res:
            continue
        else:
            temp = res + char_list[idx]
        no_repetition_sequences_helper(char_list, n - 1, temp)


def parentheses(n):
    """
    gets an integer n and returns a list with all the strings with n valid
    pairs of Parenthesis
    :param n: an integer
    :return: a list with all the strings with n valid pairs of Parenthesis
    """
    if n <= 0:
        return [""]
    option = [''] * n * 2
    lst = []
    parentheses_helper(n, option, 0, 0, 0, lst)
    return lst


def parentheses_helper(n, option, pos, start, stop, lst):
    """
    gets an integer n and returns a list with all the strings with n valid
    pairs of Parenthesis
    :param n: an integer
    :param option: one option of combination of parenthesis
    :param pos: the position inside the option
    :param start: the start position to check
    :param stop: the end position to check
    :param lst: the list that would contain the options
    :return: the updated list containing the options
    """
    if stop == n:
        lst.append("".join(option))
    else:
        if start > stop:
            option[pos] = ')'
            parentheses_helper(n, option, pos + 1, start, stop + 1, lst)
        if start < n:
            option[pos] = '('
            parentheses_helper(n, option, pos + 1, start + 1, stop, lst)


def flood_fill(image, start):
    """
    gets an image of dots and asterisks, and start position. the function calls
    a helping function that changes the right sots to asterisks
    :param image: a list of lists containing asterisks and dots
    :param start: a tuple indicating the start position
    :return: None
    """
    x = start[0]
    y = start[1]
    flood_fill_helper(image, x, y)


def flood_fill_helper(image, x, y):
    """
    gets an image and updates it
    :param image: a list of lists containing asterisks and dots
    :param x: the X of the start location
    :param y: the Y of the start location
    :return: None
    """
    if image[x][y] == '*':
        return
    if image[x][y] != '*':
        image[x][y] = '*'
        flood_fill_helper(image, x + 1, y)
        flood_fill_helper(image, x, y + 1)
        flood_fill_helper(image, x - 1, y)
        flood_fill_helper(image, x, y - 1)
