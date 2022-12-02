# Rock paper scissor scoring
# Get my total score if I follow the directions

with open('day-02-input.txt') as file:
    guide = [line.strip() for line in file]


rock_x = 1
paper_y = 2
scissors_z = 3

# a = rock
# b = paper
# c = scissors

lose = 0
draw = 3
win = 6


fake_guide = (
    'A Y',  # 8 = 0 + 2 + 6
    'B X',  # 1
    'C Z',  # 6
        )

total_score = 0

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
    elif game in ('B X', 'C Y', 'A Z'):
        total_score += 0

# Part 1:
print(total_score)

# Part 2:
