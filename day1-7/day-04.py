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

# Part 1: In how many assignment pairs does one range fully contain the other?

all_embodied = 0

for str_pair in all_pairs:
    sections = []
    split_pair = str_pair.split(",")
    for pair in split_pair:
        section = pair.split("-", 2)
        sections.extend(section)

    int_sect = [int(sect) for sect in sections]

    # a_start, a_end, b_start, b_end = int_sect[0], int_sect[1], int_sect[2], int_sect[3]
    # Below: destructured version
    a_start, a_end, b_start, b_end = int_sect

    #if one embodies another
    if ((a_start <= b_start) and (a_end >= b_end)) or \
            ((a_start >= b_start) and (a_end <= b_end)):
        all_embodied += 1


# print(total)
print(f"all embodied: {all_embodied}")
# section = [pair for pair in split_pair.split("-", 2)]
# print(f"section {section}")

# Part 2:
len_all_pairs = len(all_pairs)
no_overlap = 0

for str_pair in all_pairs:
    sections = []
    split_pair = str_pair.split(",")
    for pair in split_pair:
        section = pair.split("-", 2)
        sections.extend(section)
    int_sect = [int(sect) for sect in sections]
    a_start, a_end, b_start, b_end = int_sect
    if (a_end < b_start) or (b_end < a_start):
        no_overlap += 1

overlaps = len_all_pairs - no_overlap

print(f"all overlaps: {overlaps}")


# replace '-' with ','
for str_pair in all_pairs:
    # replacing - to , in order to split all by ",".
    version_1 = [int(sect) for sect in str_pair.replace('-', ',').split(',')]
    # second version:
    version_2 = [int(sect) for r in str_pair.split(',') for sect in r.split('-')]

    print(list_sections)
