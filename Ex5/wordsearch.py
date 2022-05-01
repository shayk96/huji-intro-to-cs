#################################################################
# FILE : wordsearch.py
# WRITER : shay kvasha , shayk96
# EXERCISE : intro2cse ex5 2020
# DESCRIPTION: a little program that finds words in a 2D matrix
#################################################################
from os import path
import sys
from collections import Counter


CORRECT_NUMBER_OF_ARGUMENTS = 4
POSSIBLE_DIRECTIONS = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}


def check_input_args(args):
    """
    checks the validity of the arguments inputted by the user
    :param args: list of arguments
    :return: either an informative error massage or the value None
    """
    if len(args) != CORRECT_NUMBER_OF_ARGUMENTS:
        return 'Error, pls insert 4 parameters'
    elif not path.isfile(args[0]):
        return 'Word file do not exists'
    elif not path.isfile(args[1]):
        return 'Matrix file do not exists'
    for direction in args[3]:
        if direction not in POSSIBLE_DIRECTIONS:
            return 'Wrong search directions'
    else:
        return None


def read_wordlist_file(filename):
    """
    opens the file that contains words and translates it to a list
    :param filename: the file containing words
    :return: a list of words
    """
    with open(filename) as word_lst:
        word_lst = word_lst.read().splitlines()
    return word_lst


def wordlist_helper(word_lst):
    """
    converts the word list to a set
    :param word_lst:
    :return: a set of the words to be searched for
    """
    word_lst = set(word_lst)
    return word_lst


def read_matrix_file(filename):
    """
    opens the file that contains the matrix and translates it to a list of
    lists
    :param filename: the file containing the matrix
    :return: a list of list containing the matrix
    """
    mat_file = open(filename, 'r')
    raw_matrix = [(line.strip()).split(',') for line in mat_file]
    mat_file.close()
    return raw_matrix


def matrix_helper(raw_matrix):
    """
    eliminates all the unneeded commas and apostrophes from the row matrix list
    of lists
    :param raw_matrix: the matrix with commas and apostrophes
    :return: matrix without commas and apostrophes
    """
    matrix = []
    for row in range(len(raw_matrix)):
        matrix.append(["".join(raw_matrix[row]).replace(',', '')])
    return matrix


def create_diagonals(matrix):
    """
    creates a list of lists that contains the diagonals from the matrix
    :param matrix: a list of lists of letters that makes the 2D matrix
    :return: a list of lists that contains the diagonals from the matrix
    """
    matrix = [row for rows in matrix for row in rows]
    width, height = len(matrix[0]), len(matrix)

    def diag(ssx, ssy):
        for x, y in zip(range(ssx, height), range(ssy, width)):
            yield matrix[x][y]

    for sx in range(height):
        yield list(diag(sx, 0))
    for sy in range(1, width):
        yield list(diag(0, sy))


def search_engine_diagonal(matrix, word_set):
    """
    searches for the words that are diagonal inside the matrix
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found in the matrix
    """
    matrix = list(create_diagonals(matrix))
    found_lst = []
    for diag in range(len(matrix)):
        for idx in range(len(matrix[0])):
            for next_idx in range(idx, len(matrix[0]) + 1):
                if idx == next_idx or len(matrix[diag]) < next_idx:
                    continue
                if "".join(matrix[diag][idx:next_idx]) in word_set:
                    found_lst.append("".join(matrix[diag][idx:next_idx]))
    return found_lst


def search_engine(matrix, word_set):
    """
    searches for the words that are inside the matrix
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found in the matrix
    """
    found_lst = []
    for row in range(len(matrix)):
        for idx in range(len(matrix[0][0])):
            for next_idx in range(idx, (len(matrix[0][0]) + 1)):
                if (matrix[row][0][idx:next_idx]) in word_set:
                    found_lst.append(matrix[row][0][idx:next_idx])
    return found_lst


def direction_right(matrix, word_set):
    """
    makes the search engine look for words from right to left
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    direction_r = search_engine(matrix, word_set)
    return direction_r


def direction_left(matrix, word_set):
    """
    makes the search engine look for words from left to right
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_left_direction = []
    for row in matrix:
        matrix_for_left_direction.append([row[0][::-1]])
    direction_l = search_engine(matrix_for_left_direction, word_set)
    return direction_l


def direction_down(matrix, word_set):
    """
    makes the search engine look for words from top to bottom
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_down_direction = []
    for i in range(len(matrix[0][0])):
        matrix_for_down_direction.append(
            [''.join(row[0][i] for row in matrix)])
    direction_d = search_engine(matrix_for_down_direction, word_set)
    return direction_d


def direction_up(matrix, word_set):
    """
    makes the search engine look for words from the bottom up
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_up_direction = []
    matrix = matrix[::-1]
    for i in range(len(matrix[0][0])):
        matrix_for_up_direction.append([''.join(row[0][i] for row in matrix)])
    direction_u = search_engine(matrix_for_up_direction, word_set)
    return direction_u


def direction_right_down(matrix, word_set):
    """
    makes the search engine look for words diagonally from the top to the
    bottom right
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    direction_rd = search_engine_diagonal(matrix, word_set)
    return direction_rd


def direction_right_up(matrix, word_set):
    """
    makes the search engine look for words diagonally from the bottom to the
    top right
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_right_up = matrix[::-1]
    direction_ru = search_engine_diagonal(matrix_for_right_up, word_set)
    return direction_ru


def direction_left_down(matrix, word_set):
    """
    makes the search engine look for words diagonally from the top to the
    bottom left
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_left_down = []
    for row in matrix:
        matrix_for_left_down.append([row[0][::-1]])
    direction_ld = search_engine_diagonal(matrix_for_left_down, word_set)
    return direction_ld


def direction_left_up(matrix, word_set):
    """
    makes the search engine look for words diagonally from the bottom to the
    top left
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: the words found
    """
    matrix_for_left_up = []
    matrix = matrix[::-1]
    for row in matrix:
        matrix_for_left_up.append([row[0][::-1]])
    direction_lu = search_engine_diagonal(matrix_for_left_up, word_set)
    return direction_lu


def word_search(directions, matrix, word_set):
    """
    gets the directions and initializes the corresponding functions
    :param directions: the directions to the matrix to check for words
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param word_set: the words to look up in the matrix
    :return: a list of all the words found
    """
    words_found_in_matrix = []
    if matrix:
        if 'r' in directions:
            words_found_in_matrix.append(direction_right(matrix, word_set))
        if 'l' in directions:
            words_found_in_matrix.append(direction_left(matrix, word_set))
        if 'u' in directions:
            words_found_in_matrix.append(direction_up(matrix, word_set))
        if 'd' in directions:
            words_found_in_matrix.append(direction_down(matrix, word_set))
        if 'w' in directions:
            words_found_in_matrix.append(direction_right_up(matrix, word_set))
        if 'x' in directions:
            words_found_in_matrix.append(direction_left_up(matrix, word_set))
        if 'y' in directions:
            words_found_in_matrix.append(
                direction_right_down(matrix, word_set))
        if 'z' in directions:
            words_found_in_matrix.append(direction_left_down(matrix, word_set))
        return words_found_in_matrix
    else:
        return words_found_in_matrix


def find_words_in_matrix(word_set, matrix, directions):
    """
    calls the functions that search for the words
    :param word_set: the words to look up in the matrix
    :param matrix: a list of lists of letters that makes the 2D matrix
    :param directions: the directions to the matrix to check for words
    :return: the final list of words to be written to the output file
    """
    matrix = matrix_helper(matrix)
    words_found_in_matrix = word_search(directions, matrix, word_set)
    final_results = convert_list_to_tuple(words_found_in_matrix)
    return final_results


def convert_list_to_tuple(words_found_in_matrix):
    """
    converts the elements of the list to tuples
    :param words_found_in_matrix: the list of words found in the matrix
    :return: a list of tuples each tuple containing the word and how many
    times it was found
    """
    words_found_in_matrix = [item for items in words_found_in_matrix for item
                             in items]
    words_found_in_matrix = list(Counter(words_found_in_matrix).items())
    return words_found_in_matrix


def write_output_file(results, output_filename):
    """
    writes the words found to a file of the user choosing
    :param results: a list containing tuples, each tuple containing a ward
    found and how many times it was found
    :param output_filename: the name of the file to write the results to
    :return: nothing
    """
    with open(output_filename, 'w') as output_file:
        output_file.write("\n".join([','.join(map(str, item)) for item
                                     in results]))
        if len(results) != 0:
            output_file.write("\n")
        else:
            pass


def main():
    """
    the main function that initializes all the function as needed
    :return: nothing
    """
    if check_input_args(sys.argv[1:]) is None:
        word_file = sys.argv[1]
        matrix_file = sys.argv[2]
        output_file = sys.argv[3]
        directions_to_check = sys.argv[4]
        word_lst = read_wordlist_file(word_file)
        word_set = wordlist_helper(word_lst)
        not_matrix = read_matrix_file(matrix_file)
        matrix = matrix_helper(not_matrix)
        if matrix:
            words_found = find_words_in_matrix(word_set, matrix,
                                               directions_to_check)
            write_output_file(words_found, output_file)
        else:
            write_output_file([], output_file)
    else:
        print(check_input_args(sys.argv[1:]))


if __name__ == '__main__':
    main()
