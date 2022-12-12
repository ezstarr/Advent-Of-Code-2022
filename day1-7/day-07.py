with open('day-07-example.txt') as file:
    # strip removes spaces before and after the str
    # split turns string into a list. Default arg is whitespace
    # it's better to use file.readlines() than read.split("\n")
    # because windows sometimes uses "\r\n" instead of just "\n" and readlines handles that
    ex_output = [line for line in file.readlines()]
    alt_syntax = [line for line in file.read().splitlines()]

# this is a list comprehension, strips the \n
output_lines = list(map(str.strip, ex_output))


files: dict[str, int] = {}  # {'filename': size->int}
dirs: dict[str, int] = {}
cmd: list[str] = ['/']

for line in output_lines:
    # example return: ['$', 'cd', '/']
    line_list = line.split()
    print(line_list)

    # add to file:
    # if line_list[0].isdigit():
    if line_list[0].isnumeric(): # .isdecimal() also works
        # if ['14848514', 'b.txt']
        # then files = {'b.txt':'14848514'}
        files[line_list[1]] = int(line_list[0])


    # create dict of abs paths: dirs = {'/a': 0, '/a/d/': 0, '/d': 0, '/d/r': 0 }

    if line_list[0] == "dir":
        if dirs == {}:
            dir_name = '/' + line_list[1]
            dirs["/" + dir_name] = 0
        else:
            pass

    # add to cmd:
    if

print(files)