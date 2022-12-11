with open('day-07-input.txt') as file:
    # strip removes spaces before and after the str
    # split turns string into a list. Default arg is whitespace
    # it's better to use file.readlines() than read.split("\n")
    # because windows sometimes uses "\r\n" instead of just "\n" and readlines handles that
    ex_output = [line for line in file.readlines()]
    alt_syntax = [line for line in file.read().splitlines()]

output_lines = list(map(str.strip, ex_output))

cur_dir = ["/"]  # each index is a directory, gets added on line 26 ["/", "a", "e"]
dir_sizes = {tuple(cur_dir): 0}  # directory->key, filesize-> value

for line in output_lines:
    line_list = line.split()
    # print(line_list)

    # get the current directory, following commands
    if line_list[1] == 'cd':
        cur_arg = line_list[2]
        if cur_arg == "/":
            cur_dir = ["/"]
        elif cur_arg == '..':
            cur_dir.pop()
        else:
            cur_dir.append(cur_arg)

    # the file size, to add to current directory
    if line_list[0].isdigit():
        filesize = int(line_list[0])

        for i in range(len(cur_dir)):  # [('/'), ('a')]

            current_path = tuple(cur_dir[:i+1])
            # i = 0, ('/',)
            # 1 = 1, ('/', 'a',)

            if current_path not in dir_sizes:
                dir_sizes[current_path] = filesize
            else:
                dir_sizes[current_path] += filesize




sum_dirs_under100k = 0
for k, v in dir_sizes.items():
    if v <= 100_000:
        sum_dirs_under100k += v

print(cur_dir)
print(dir_sizes)



# Part 2
# Find the smallest directory I could delete, that would free up 30_000_000 sizes

# Find sum of all directories:



# difference = (70_000_000 - dir_sizes[('/',)])
root_size = dir_sizes[('/',)]

disk_space = 70_000_000
run_space = 30_000_000

avail_space = disk_space - root_size
print(avail_space)

need_freed = run_space - avail_space
print(need_freed)

# Find smallest directory bigger with size bigger than or equal-to than need_freed

potential_sizes = []
for k,v in dir_sizes.items():
    if v >= need_freed:
        potential_sizes.append(v)

smallest_dir_size_i_can_delete = min(potential_sizes)


print(smallest_dir_size_i_can_delete)

