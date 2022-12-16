with open('day-08-input.txt') as file:
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


def check_top(matrix, row, col):
    check_row = 0
    cur = tree_array[row][col]
    top = tree_array[check_row][col]

    blocks_tree = 0

    if check_row == row:
        return blocks_tree

    if cur <= top:
        blocks_tree += 1
        return blocks_tree

    while cur - top > 0 and check_row != row:
        check_row += 1
        top = tree_array[check_row][col]

        if check_row == row:
            return blocks_tree

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

    if check_col == col:
        return blocks_tree
    if cur <= right:
        blocks_tree += 1
        return blocks_tree

    while cur - right > 0 and check_col != col:
        check_col -= 1
        right = tree_array[row][check_col]

        if check_col == col:
            return blocks_tree

        if cur <= right:
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

    if check_col == col:
        return blocks_tree

    if left >= cur:
        blocks_tree += 1
        return blocks_tree

    while cur - left > 0 and check_col != col:
        check_col += 1
        left = tree_array[row][check_col]

        if check_col == col:
            return blocks_tree

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

    if check_row == row:
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


num_total_trees = 0
are_blocked = 0

for r, tree_row in enumerate(tree_array):
    for c, tree in enumerate(tree_row):
        num_total_trees += 1
        if (
                check_top(tree_array, r, c) == 0 or
                check_right(tree_array, r, c) == 0 or
                check_left(tree_array, r, c) == 0 or
                check_bottom(tree_array, r, c) == 0
        ):
            pass
        else:
            # print(f" this tree is blocked {r}, {c}")
            are_blocked += 1

visible_trees = num_total_trees - are_blocked
print(visible_trees)

# ==================== Part 2 ===========================


def get_top_view(matrix, row, col):
    view = 0
    for i in range(1, len(tree_array)+1):
        top_row = row - i
        cur = tree_array[row][col]
        top_tree = tree_array[top_row][col]

        if top_row == -1:
            return view

        view += 1

        if top_row == -1 or top_tree >= cur:
            return view



def get_right_view(matrix, row, col):
    view = 0
    for i in range(1, len(tree_row)+1):
        right_col = col + i
        if right_col > len(tree_row) - 1:
            return view

        cur = tree_array[row][col]
        right_tree = tree_array[row][right_col]

        view += 1

        if right_tree >= cur:
            return view

        if right_col == len(tree_array)-1:
            return view


def get_left_view(matrix, row, col):
    view = 0
    for i in range(1, len(tree_row)+1):
        left_col = col - i

        if left_col < 0:
            return view

        cur = tree_array[row][col]
        left_tree = tree_array[row][left_col]

        view += 1

        if left_tree >= cur or left_col < 0:
            return view


def get_bottom_view(matrix, row, col):
    view = 0
    for i in range(1, len(tree_array)):
        bottom_row = row + i

        if bottom_row > len(tree_array) - 1:
            return view

        cur = tree_array[row][col]
        bottom_tree = tree_array[bottom_row][col]

        view += 1

        if bottom_row > len(tree_array) - 1 or bottom_tree >= cur:
            return view

all_scores = []


def get_views_multiplied(matrix):
    for r, tree_row in enumerate(tree_array):
        for c, tree in enumerate(tree_row):

            top_view = get_top_view(tree_array, r, c)
            right_view = get_right_view(tree_array, r, c)
            bottom_view = get_bottom_view(tree_array, r, c)
            left_view = get_left_view(tree_array, r, c)


            tree_scenic_score = top_view * right_view * bottom_view * left_view

            # print(f"  {tree_array[r][c]}, row {r}, col {c} = {tree_scenic_score}")

            all_scores.append(tree_scenic_score)
    return all_scores

get_views_multiplied(tree_array)

print(max(all_scores))