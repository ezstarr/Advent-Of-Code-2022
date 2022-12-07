# 5.py
#
# run like this:
# $ python3 5.py 5.txt
#

import sys
import string
import re

filename = sys.argv[1]

f = open(filename)
allcrates = []
lines = f.read()
# split the file into crates and instructions
[crates,instrs] = lines.split('\n\n')



# parse crates
for line in crates.split('\n'):
    print(line)
    i = 1
    # check every 4th character in the line (where the letters are)
    while i < len(line):
        if line[i] in string.ascii_uppercase: # if its an uppercase letter
        # get crate index - integer division by 4
        idx = i // 4
        # loop adding an empty list to allcrates until idx is within 0..len(allcrates)-1
        while idx >= len(allcrates):
            allcrates.append([])
        # now its safe to access allcrates[idx]
        allcrates[idx].append(line[i])
        i += 4
# reverse each crate so that pop() works
for crate in allcrates:
    crate = crate.reverse()

# process instructions
for instr in instrs.split('\n'):
    if len(instr) == 0:
        continue
    # filter out numbers by using a regex.
    # this just splits the line by spaces or any of these letters
    # then filters out empty strings
    nums = filter(len, re.split(' |m|o|v|e|f|r|t', instr))
    # turn the 3 numbers into ints
    [num_moves ,from_,to] = map(int, nums)
    # move the crates around
    for _ in range(num_moves):
      allcrates[to-1].append(allcrates[from_-1].pop())

# print them out
print(''.join([crate[-1] for crate in allcrates]))