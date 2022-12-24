with open('day-03-input.txt') as file:
    all_rucksacks = [line.strip() for line in file]

# Part 2:
"""
Elves in groups of 3
One badge - only item carried by all 3, nothing else is carried by all 3
What is the sum of the priorities of those item types?
"""

badge_priorities = 0

lower_difference = 96
upper_difference = 38


# A generator function to yield a group.
# It's a generator because it uses yield instead of returning a list of lists
# No stored memory.
def group(rucksacks):
    for i in range(0, len(all_rucksacks), 3):
        a_group = all_rucksacks[i:i + 3]
        yield a_group


def get_priority_of_letters(letter):
    if letter.islower():
        return ord(letter) - lower_difference
    else:
        return ord(letter) - upper_difference


# a, b, c are names given to each line in the "group" of 3.
for a, b, c in group(all_rucksacks):
    common_character = (set(a) & set(b) & set(c)).pop()
    badge_priorities += get_priority_of_letters(common_character)

print(badge_priorities)
