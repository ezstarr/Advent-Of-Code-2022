with open('day-02-input.txt') as file:
    guide = [line.strip() for line in file]

# Part 2:

# Actual instructions say second element (XYZ) tells my required outcome:
# x = lose  # 0 points
# y = draw  # 3 points
# z = win  # 6 points

rock_x = 1
paper_y = 2
scissors_z = 3

# First element tells what opponent will play:
# a = rock
# b = paper
# c = scissors

# Same scoring system as part 1
# Total number of points won from all the games:
total_score_2 = 0

for game in guide:
    if 'Z' in game:
        total_score_2 += 6
    elif 'Y' in game:
        total_score_2 += 3
    # rock means +1 (win, draw, lose)
    if game in ('C Z', 'A Y', 'B X'):
        total_score_2 += 1
    if game in ('A Z', 'B Y', 'C X'):
        total_score_2 += 2
    if game in ('B Z', 'C Y', 'A X'):
        total_score_2 += 3

print(total_score_2)