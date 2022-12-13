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
    i = 1
    up_row = (row - i)
    cur = tree_array[row][col]
    up = tree_array[up_row][col]
    print(f"cur: {cur}, up: {up}")

    while up_row > 0:
        if cur >= up:
            print(f" cur >= up: {cur >= up}")
            print(f" -first up_row: {up_row}")
            i += 1
            up_row = row - i
            print(f" -next up_row: {up_row}")
            print(f"  i equals {i}, row equals: {row}")
            up = tree_array[up_row][col]
            print(f"   cur: {cur}, up: {up}")
            print(f"    cur >= up: {cur >= up}")
        if up_row == 0:
            visible = True
            print(visible)
        else:
            print("not visible")




def check_right(matrix, row):
    pass


def check_left(matrix, row):
    pass


def check_bottom(matrix, col):
    pass


# print(tree_array[(-1)-2][2] == tree_array[2][2])

print(check_top(tree_array, 2, 0))
