# How many calories are being carried by the elf carrying the most calories?

# Progression:
# For-loop
# IndexError when indexing out of range
# Now attempting to use functions to work around it <-- current
# Next: Review how to stay in range using operations instead of enumeration etc.

# WIP: NO ONE LOOK AT BELOW CODE XD

with open('day-01-input.txt') as file:
    string_list = [line.strip() for line in file]


converted_data = []
grouped_data = []
totals = []


for string_line in string_list:
    if string_line == '':
        string_line = 0
    int_line = int(string_line)
    converted_data.append(int_line)

def get_a_group(food_cal_list):

    one_elf = []
    one_elf_sum = 0
    for food in food_cal_list:
        if food > 0:
            one_elf.append(food)
        else:
            break
    print(one_elf)
    for item in one_elf:
        one_elf_sum += item

    return one_elf_sum




print(get_a_group(converted_data))
