with open('day-04-input.txt') as file:
    all_pairs = [line.strip() for line in file]

fake_pairs = [
    '2-4, 6-8',
    '2-3, 4-5',
    '5-7, 7-9',
    '2-8, 3-7',
    '6-6, 4-6',
    '2-6, 4-8',
]

# In how many assignment pairs does one range fully contain the other?


total = 0

# for str_pair in all_pairs:
#     sections = []
#
#     split_pair = str_pair.split(",")
#
#     # print(f"split pair {split_pair}")
#     for pair in split_pair:
#         section = pair.split("-", 2)
#         sections.extend(section)
#     # print(sections)
#     a_start = int(sections[0])
#     a_end = int(sections[1])
#     b_start = int(sections[2])
#     b_end = int(sections[3])

    # if one embodies another
    # if ((a_start <= b_start) and (a_end >= b_end)) or \
    #         ((a_start >= b_start) and (a_end <= b_end)):
    #     total += 1


# print(total)
print(total)
# section = [pair for pair in split_pair.split("-", 2)]
# print(f"section {section}")

# Part 2:
len_all_pairs = len(all_pairs)
no_overlap = 0

for str_pair in all_pairs:
    sections = []

    split_pair = str_pair.split(",")

    # print(f"split pair {split_pair}")
    for pair in split_pair:
        section = pair.split("-", 2)
        sections.extend(section)
    # print(sections)
    a_start = int(sections[0])
    a_end = int(sections[1])
    b_start = int(sections[2])
    b_end = int(sections[3])
    if (a_end < b_start) or (b_end < a_start):
        no_overlap += 1

overlaps = len_all_pairs - no_overlap

print(overlaps)

