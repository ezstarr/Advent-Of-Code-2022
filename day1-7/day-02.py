# Rock paper scissor scoring
# Get my total score if I follow the directions

with open('day-02-input.txt') as file:
    guide = [line.strip() for line in file]


# Assigns points to each shape
rock_x = 1
paper_y = 2
scissors_z = 3

# a = rock
# b = paper
# c = scissors

# Assigns points to each outcome
lose = 0
draw = 3
win = 6


# Score per round based on shape + outcome
# All the scores added together
total_score = 0

# Each game's points gets added to total:
for game in guide:
    if 'Y' in game:
        total_score += 2
    if 'Z' in game:
        total_score += 3
    if 'X' in game:
        total_score += 1

    if game in ('C X', 'A Y', 'B Z'):
        total_score += 6
    elif game in ('A X', 'B Y', 'C Z'):
        total_score += 3

# Part 1:
# Total score be if everything goes exactly according to your strategy guide
print(total_score)
#The higher the score, the closer you get to sleep to snacks as an elf.


# Part 2:
# x = lose  # 0
# y = draw  # 3
# z = win  # 6

# rock_x = 1
# paper_y = 2
# scissors_z = 3

# a = rock
# b = paper
# c = scissors

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