with open('day-03-example.txt') as file:
    all_rucksacks = [line.strip() for line in file]

# This prints out the alphabet:
# for i in range(ord('a'), ord('z')+1):
#     print(chr(i)) This prints the alphabet


# value = (ord('A') - upper_difference)


    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.


lower_difference = 96
upper_difference = 38

sum_of_priorities = 0
a_priority = 0


def get_priority_of_letters(letter):
    if letter.islower():
        return ord(letter) - lower_difference
    else:
        return ord(letter) - upper_difference


# Get priority of item in a sac, to add to sum_of_priorities.
for sack in all_rucksacks:
    half = len(sack) // 2
    first_part = set(sack[half:])
    second_part = set(sack[:half])

    # this is a set intersection, known as "set_a & set_b"
    # it returns an item as a set, selected via .pop()
    a = (first_part.intersection(second_part).pop())

    sum_of_priorities += get_priority_of_letters(a)

# solution
print(sum_of_priorities)