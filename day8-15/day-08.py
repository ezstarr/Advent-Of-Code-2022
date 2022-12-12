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
print(column(tree_array, 1))

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
r_check = tree[row][len(tree_row)-1+1] <= tree[row][len(tree_row)-1+2] <= until... tree[row][col] == tree[2][2]

"""