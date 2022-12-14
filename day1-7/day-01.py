# How many calories are being carried by the elf carrying the most calories?


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


total = 0
for data in converted_data:
    if data > 0:
        total += data
    if data == 0:
        grouped_data.append(total)
        total = 0

# Part 1:
# Calories carried by the elf with the most calories
print(max(grouped_data))

# Part 2:
sorted_data = sorted(grouped_data)


top_3_total = sum(sorted_data[-3:])

# Combined calories carried by the top 3 elves
print(top_3_total)

