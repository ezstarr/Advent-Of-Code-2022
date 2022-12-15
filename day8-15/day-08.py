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
    up_row = row - 1
    cur = tree_array[row][col]
    up_tree = tree_array[up_row][col]
    print(f"cur: {cur}, up_tree: {up_tree}")

    if up_tree >= cur:
        return 0

    while up_tree < cur:
        up_row -= 1
        up_tree = tree_array[up_row][col]

        if up_tree < cur:
            up_row -= 1
            up_tree = tree_array[up_row][col]

        if up_tree <= cur:
            return row - up_row


# print(f"get top view: {get_top_view(tree_array, 4, 3)}")

def get_right_view(matrix, row, col):
    right_col = col + 1
    cur = tree_array[row][col]
    right_tree = tree_array[row][right_col]
    print(f"cur: {cur}, right_tree: {right_tree}")

    if right_tree >= cur:
        return 0

    while right_tree < cur:
        right_col += 1
        right_tree = tree_array[row][right_col]
        right_col += 1

        if right_tree >= cur:
            return right_col - col

        return right_col - col


print(f"get right view: {get_right_view(tree_array, 2, 0)}")

def get_left_view(matrix, row, col):
    up_row = row - 1
    cur = tree_array[row][col]
    up_tree = tree_array[up_row][col]
    print(f"cur: {cur}, up_tree: {up_tree}")

    if up_tree >= cur:
        return 0

    while up_tree < cur:
        up_row -= 1
        up_tree = tree_array[up_row][col]

        if up_tree < cur:
            up_row -= 1
            up_tree = tree_array[up_row][col]

        if up_tree <= cur:
            return row - up_row


def get_bottom_view(matrix, row, col):
    up_row = row - 1
    cur = tree_array[row][col]
    up_tree = tree_array[up_row][col]
    print(f"cur: {cur}, up_tree: {up_tree}")

    if up_tree >= cur:
        return 0

    while up_tree < cur:
        up_row -= 1
        up_tree = tree_array[up_row][col]

        if up_tree < cur:
            up_row -= 1
            up_tree = tree_array[up_row][col]

        if up_tree <= cur:
            return row - up_row


for r, tree_row in enumerate(tree_array):
    for c, tree in enumerate(tree_row):
        top_view = 0
        right_view = 0
        bottom_view = 0
        left_view = 0


        tree_scenic_score = top_view * right_view * bottom_view * left_view


