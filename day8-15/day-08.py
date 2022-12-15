from typing import Any

with open('day-08-example.txt') as file:
    tree_grid = [line.strip() for line in file.readlines()]

tree_array = []

for tree_row in tree_grid:
    row_list = []
    for tree in tree_row:
        int_tree = int(tree)
        row_list.append(int_tree)

    tree_array.append(row_list)

print(*tree_array, sep="\n")


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

    if row == check_row:
        return blocks_tree
    if cur <= top:
        blocks_tree += 1
        return blocks_tree

    # GET YES - VISIBLE, if cur - top > 0 --> add nothing
    # GET NO - NOT VISIBLE, if cur - top < 0 --> add 1
    while cur - top > 0 and check_row != row:

        check_row += 1

        if check_row == row:
            return blocks_tree

        top = tree_array[check_row][col]

        if top >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_row == row:
            return blocks_tree

    return blocks_tree


def check_right(matrix, row, col):
    check_col = (len(tree_row) - 1)
    cur = tree_array[row][col]
    right = tree_array[row][check_col]

    blocks_tree = 0

    if col == check_col:
        return blocks_tree

    if cur <= right:
        blocks_tree += 1
        return blocks_tree

    while cur - right > 0 and check_col != col:

        check_col -= 1

        if check_col == col:
            return blocks_tree

        right = tree_array[row][check_col]

        if cur <= right:
            blocks_tree += 1
            return blocks_tree

        if col == check_col:
            return blocks_tree


    return blocks_tree


def check_left(matrix, row, col):
    check_col = 0
    cur = tree_array[row][col]
    left = tree_array[row][check_col]

    blocks_tree = 0

    if col == check_col:
        return blocks_tree

    elif left >= cur:
        blocks_tree += 1
        return blocks_tree

    while cur - left > 0 and check_col != col:

        check_col += 1
        left = tree_array[row][check_col]

        if left >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_col == col:
            return blocks_tree

    return blocks_tree


def check_bottom(matrix, row, col):
    check_row = len(tree_array) - 1
    cur = tree_array[row][col]
    bottom = tree_array[check_row][col]

    blocks_tree = 0

    if row == check_row:
        return blocks_tree

    if cur <= bottom:
        blocks_tree += 1
        return blocks_tree

    while cur - bottom > 0 and check_row != row:

        check_row -= 1

        if check_row == row:
            return blocks_tree

        bottom = tree_array[check_row][col]

        if bottom >= cur:
            blocks_tree += 1
            return blocks_tree

        if check_row == row:
            return blocks_tree

    return blocks_tree


num_visible_trees = 0

for row, tree_row in enumerate(tree_array):
    for col, tree in enumerate(tree_row):
        num_blocks = 0
        print(f"==== row: {row}, col: {col}")
        if check_top(tree_array, row, col) == 0:
            print(check_top(tree_array, row, col))
            print(f"    top visible")
        else:
            print(check_top(tree_array, row, col))
            print(f"    top blocked")
            num_blocks += 1

        if check_right(tree_array, row, col) == 0:
            print(check_right(tree_array, row, col))
            print(f"    right visible")
        else:
            print(check_right(tree_array, row, col))
            print(f"    right blocked")
            num_blocks += 1

        if check_left(tree_array, row, col) == 0:
            print(check_left(tree_array, row, col))
            print(f"    left visible")
        else:
            print(check_left(tree_array, row, col))
            print(f"     left blocked")
            num_blocks += 1

        if check_bottom(tree_array, row, col) == 0:
            print(check_bottom(tree_array, row, col))
            print(f"    bottom visible")
        else:
            print(check_bottom(tree_array, row, col))
            print(f"     bottom blocked")
            num_blocks += 1

        # if (
        #         check_top(tree_array, row, col) == 0 or
        #         check_right(tree_array, row, col) == 0 or
        #         check_left(tree_array, row, col) == 0 or
        #         check_bottom(tree_array, row, col) == 0
        #         ):
        print(f"num_blocks: {num_blocks}")
        if num_blocks < 4:
            num_visible_trees += 1


print(num_visible_trees)


row = 1
col = 3
four_checks = (check_top(tree_array, row, col) == 0  # or
               # check_right(tree_array, row, col) == 0 or
               # check_left(tree_array, row, col) == 0 or
               # check_bottom(tree_array, row, col) == 0
               )
print(four_checks)

print("================")
print(*tree_array, sep="\n")
