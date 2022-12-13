from typing import Any

with open('day-08-example.txt') as file:
    tree_grid = [line.strip() for line in file.readlines()]

row = 0
col = 0
visible_tree_count = 0

tree_array = []

for tree_row in tree_grid:
    row_list = []
    for tree in tree_row:
        int_tree = int(tree)
        row_list.append(int_tree)

    tree_array.append(row_list)

print(*tree_array, sep="\n")


def column(matrix, col):
    return [tree_row[col] for tree_row in matrix]


print("================")
# print(column(tree_array, 1))

# for each tree[row][col],
# check the left, top, right, bottom
# left_start = tree[row][0]
# top_start = tree[0][col]
# right_start = tree[row][len(tree_row)-1]
# bottom_start = tree[len(tree_array)-1][0]

# example
"""
hint: the "int" needs to to change (0 or len(tree_array)-1)
    
    for tree[2][2] -> 3 

t_check = tree[0][2] <= tree[1][2] <= tree[2][2], then ok. 
    // row + 1
r_check = tree[2][(-1)-1] <= tree[2][(-1)-1] <= until... == tree[2][2]
    // col - 1
l_check = tree[2][0] <= tree[2][0+1] <= tree[2][0+2] <= tree[2][2]
    // col + 1
b_check = tree[(-1)][2] <= tree[(-1)-2][2] <= tree[2][2]
    // row - 1
    
"""


def check_top(matrix, row, col):
    check_row = 0
    cur = tree_array[row][col]
    top = tree_array[check_row][col]

    blocks_tree = 0

    if row == 0:
        blocks_tree += 0

    # GET YES - VISIBLE, if cur - top > 0 --> add nothing
    # GET NO - NOT VISIBLE, if cur - top < 0 --> add 1
    while check_row >= 0 and check_row != row:

        if cur > top:
            # Current row is taller than check_row
            # blocks_tree += 0

            blocks_tree += 0

            check_row += 1

            if check_row == row:
                return blocks_tree

            top = tree_array[check_row][col]

            blocks_tree += 0


        if top >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_row == row:
            return blocks_tree

    return blocks_tree


def check_right(matrix, row, col):
    check_col = (len(tree_row)-1)
    cur = tree_array[row][col]
    right = tree_array[row][check_col]

    blocks_tree = 0

    if col == check_col:
        blocks_tree += 0

    while cur - right > 0 and check_col != col:

        if cur > right:
            blocks_tree += 0
            check_col -= 1

            if check_col == col:
                return blocks_tree

            right = tree_array[row][check_col]
            blocks_tree += 0

        if right >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_col == col:
            return blocks_tree

    return blocks_tree


def check_left(matrix, row, col):
    check_col = 0
    cur = tree_array[row][col]
    left = tree_array[row][check_col]

    blocks_tree = 0

    if col == check_col:
        blocks_tree += 0

    while cur - left > 0 and check_col != col:

        if cur > left:
            blocks_tree += 0
            check_col += 1

            if check_col == col:
                return blocks_tree

            left = tree_array[row][check_col]
            blocks_tree += 0

        if left >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_col == col:
            return blocks_tree

    return blocks_tree


def check_bottom(matrix, row, col):
    check_row = len(tree_array)-1
    cur = tree_array[row][col]
    bottom = tree_array[check_row][col]

    blocks_tree = 0

    if row == check_row:
        blocks_tree += 0

    while cur - bottom > 0 and check_row != row:

        if cur > bottom:
            blocks_tree += 0
            check_row -= 1

            if check_row == row:
                return blocks_tree

            bottom = tree_array[check_row][col]
            blocks_tree += 0

        if bottom >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_row == row:
            return blocks_tree

    return blocks_tree


for