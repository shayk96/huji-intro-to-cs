###############################################################################
# FILE : nonogram.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex8 2020
# DESCRIPTION: a little program that solves nonogram
# SITES USED: https://stackoverflow.com/
# I chose to leave an UNKNOWN TILE because the way my function works is that it
# goes over and over the lines until it sees that nothing changed between two
# times, but many times it leaves a tile in an unknown state and figures it out
# later. That's why i chose to leave it in an UNKNOWN TILE state
###############################################################################
from math import factorial

WHITE_TILE = 0
BLACK_TILE = 1
UNKNOWN_TILE = -1
COLUMN_CONSTRAINTS = 1
ROW_CONSTRAINTS = 0


def get_row_variations(row, blocks):
    """
    accepts the data given in the table and its constraints (list of block
    sizes) and return a list of all the options for coloring the line so that
    the coloring will meet the constraints
    :param row: the row in the nonogram being checked
    :param blocks: the number of colored tiles and how they are arranged
    :return: a list of all coloring options for the row
    """
    var = []
    all_var = []
    if len(row) == 0:
        return [[]]
    num_of_var = count_row_variations(len(row), blocks)
    get_row_variations_helper(row, blocks, var, all_var, num_of_var)
    return all_var


def get_row_variations_helper(row, blocks, var, all_var, num_of_var, i=0):
    """
    a helping function that returns all the options for coloring the row
    :param row: the row in the nonogram being checked
    :param blocks: the number of colored tiles and how they are arranged
    :param var: current option being constructed
    :param all_var: a list of options
    :param num_of_var: the number of possible solutions
    :param i: used to advance the index
    :return: a list of all coloring options for the row
    """
    if len(all_var) == num_of_var + 1:
        return
    if len(var) == len(row):
        if check_blocks(var, blocks):
            return all_var.append(var)
        else:
            return
    if len(row) != 1 and UNKNOWN_TILE not in row:
        all_var.append(row)
        return
    if var.count(BLACK_TILE) > sum(blocks) or \
            var.count(WHITE_TILE) > len(row) - sum(blocks):
        return
    if row[i] == WHITE_TILE:
        get_row_variations_helper(row, blocks, var + [WHITE_TILE], all_var,
                                  num_of_var, i + 1)
    if row[i] == BLACK_TILE:
        get_row_variations_helper(row, blocks, var + [BLACK_TILE], all_var,
                                  num_of_var, i + 1)
    if row[i] == UNKNOWN_TILE:
        get_row_variations_helper(row, blocks, var + [WHITE_TILE], all_var,
                                  num_of_var, i + 1)
        get_row_variations_helper(row, blocks, var + [BLACK_TILE], all_var,
                                  num_of_var, i + 1)


def check_blocks(var, blocks):
    """
    checks if the solution is in line with the blocks
    :param var: the solution
    :param blocks: the number of colors tiles and their grouping
    :return: True if the solution is in line, else False
    """
    count = 0
    res = []
    for i in range(len(var)):
        if i == len(var) - 1:
            if var[i] == BLACK_TILE:
                count += 1
                res.append(count)
        if var[i] == BLACK_TILE:
            count += 1
        else:
            if count != 0:
                res.append(count)
                count = 0
            else:
                count = 0
    if len(res) == 0:
        res.append(len(var))
    if res == blocks:
        return True
    else:
        return


def get_intersection_row(rows):
    """
    gets all the possible solutions for a row and combines them to a single
    option. if a final solution cant be reached it leaves -1 in the row.
    :param rows: possible solutions for the row
    :return: a final solution
    """
    ans = []
    if len(rows) != 0:
        matching_idx = []
        for idx in range(len(rows[0])):
            matching_idx.append([item[idx] for item in rows])
        for i in range(len(matching_idx)):
            if matching_idx[i].count(WHITE_TILE) == len(matching_idx[i]):
                ans.append(WHITE_TILE)
            elif matching_idx[i].count(BLACK_TILE) == len(matching_idx[i]):
                ans.append(BLACK_TILE)
            else:
                ans.append(UNKNOWN_TILE)
        return ans
    else:
        return ans


def get_variation(lines):
    """
    receives a list of lines and their constrains and calls the functions
    that gets the possible and final solution
    :param lines: a list of either roes or columns and their constrictions
    :return: either updated rows or updated columns
    """
    updated_lines = []
    for i in range(len(lines)):
        temp = get_row_variations(lines[i][0], lines[i][1])
        if len(temp) == 0:
            updated_lines.append(lines[i][0])
        else:
            updated_lines.append(get_intersection_row(temp))
    return updated_lines


def create_rows_with_blocks(rows, constraints):
    """
    combines the list of rows with the list of constrains
    :param rows:  a list containing the rows of the nonogram
    :param constraints: a list containing the constraints of the nonogram
    :return: a combines list of rows and constraints
    """
    rows_with_blocks = list(zip(rows, constraints))
    return rows_with_blocks


def rows_to_columns(rows, constraints):
    """
    creates a list of columns
    :param rows: a list containing the rows of the nonogram
    :param constraints: a list containing the constraints of the nonogram
    :return: a list containing the columns of the monogram and their
    constraints
    """
    columns_with_blocks = []
    for idx in range(len(rows[0])):
        columns_with_blocks.append([item[idx] for item in rows])
    columns = list(zip(columns_with_blocks, constraints))
    return columns


def columns_to_rows(columns, constraints):
    """
    crates a list of rows
    :param columns: a list containing the columns of the nonogram
    :param constraints: a list containing the constraints of the nonogram
    :return: a list og rows and their constraints
    """
    rows = []
    for idx in range(len(constraints)):
        rows.append([item[idx] for item in columns])
    return rows


def check_if_solved(rows):
    """
    check if the nonogram is solved
    :param rows: a list containing the rows of the nonogram
    :return: False if not solved, else True
    """
    for i in range(len(rows)):
        if UNKNOWN_TILE in rows[i]:
            return False
    return True


def check_if_nonogram_is_legit(constraints):
    """
    checks if the nonogram can be solved
    :param constraints: a list of constraints
    :return: True if the nonogram can be solved, else False
    """
    res = False
    constraints_0 = [item for item in constraints[ROW_CONSTRAINTS]
                     for item in item]
    constraints_1 = [item for item in constraints[COLUMN_CONSTRAINTS]
                     for item in item]
    if sum(constraints_0) != sum(constraints_1):
        res = True
    return res


def count_row_variations(length, blocks):
    """
    counts how many option can a row have for coloring
    :param length: the length of the row
    :param blocks: the required number of colored tiles and their grouping
    :return: the number(integer) of possible variations
    """
    num_of_var = 0
    if sum(blocks) >= length:
        return num_of_var
    k = len(blocks)
    n = length - sum(blocks) + 1
    num_of_var = int(factorial(n) / (factorial(k) * factorial(n - k)))
    return num_of_var


def solve_easy_nonogram(constraints):
    """
    receives the constraints, calls a helper function and returns the solved
    nonogram
    :param constraints: a list of constraints
    :return: a list containing the solved nonogram
    """
    if check_if_nonogram_is_legit(constraints):
        return None
    rows = [[UNKNOWN_TILE] * len(constraints[COLUMN_CONSTRAINTS])] * \
           len(constraints[ROW_CONSTRAINTS])
    ans = solve_nonogram_helper(rows, constraints)
    return ans


def solve_nonogram_helper(rows, constraints):
    """
    the function solves the nonogram using other functions
    :param rows: a list containing the rows of the nonogram
    :param constraints: a list of constraints
    :return:
    """
    updated_rows = rows
    prev = None
    while not check_if_solved(rows):
        if prev == updated_rows:
            break
        else:
            rows_with_blocks = create_rows_with_blocks(updated_rows,
                                                       constraints[
                                                           ROW_CONSTRAINTS])
            updated_rows = get_variation(rows_with_blocks)
            prev = updated_rows
            columns_with_blocks = rows_to_columns(updated_rows,
                                                  constraints[
                                                      COLUMN_CONSTRAINTS])
            updated_columns = get_variation(columns_with_blocks)
            updated_rows = columns_to_rows(updated_columns,
                                           constraints[ROW_CONSTRAINTS])
    return updated_rows


def solve_nonogram(constraints):
    """
    receives the constraints, calls a helper function and returns the solved
    nonogram
    :param constraints: a list of constraints
    :return: a list containing the solved nonogram
    """
    ans = []
    res = solve_easy_nonogram(constraints)
    while not check_if_solved(res):
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == UNKNOWN_TILE:
                    res[i][j] = BLACK_TILE
                    break
            else:
                continue
            break
        res = solve_nonogram_helper(res, constraints)
    ans.append(res)
    return ans
