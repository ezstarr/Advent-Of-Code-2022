with open('day-05-input.txt') as file:
    instructions = file.readlines()[10:512]


# print(get_data)

stack_1 = ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q']
stack_2 = ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J']
stack_3 = ['F', 'B', 'H', 'W', 'P', 'M', 'Q']
stack4 = 'VSTDF'
stack5 = 'QLDWVFZ'
stack6 = 'ZCLS'
stack7 = 'ZBMVDF'
stack8 = 'TJB'
stack9 = 'QNBGLSPH'

stack_4 = [i for i in stack4]
stack_5 = [i for i in stack5]
stack_6 = [i for i in stack6]
stack_7 = [i for i in stack7]
stack_8 = [i for i in stack8]
stack_9 = [i for i in stack9]

# print(stack_9)

fake_1 = ['Z', 'N']
fake_2 = ['M', 'C', 'D']
fake_3 = ['P']
fake_instructions = [
        'move 1 from 2 to 1',
        'move 3 from 1 to 3',
        'move 2 from 2 to 1',
        'move 1 from 1 to 2',
        ]

real_listed = [i.split() for i in instructions]

array_instr = []


for line in real_listed:
    quantity = int(line[1])
    origin_stack = "stack_" + line[3]
    put_stack = "stack_" + line[5]
    a_stack = [quantity, origin_stack, put_stack]
    array_instr.append(a_stack)

# print(array_instr)

stacks = {'stack_1': stack_1, 'stack_2': stack_2,
          'stack_3': stack_3, 'stack_4': stack_4,
          'stack_5': stack_5, 'stack_6': stack_6,
          'stack_7': stack_7, 'stack_8': stack_8,
          'stack_9': stack_9}

# stacks = {'fake_1': fake_1, 'fake_2': fake_2, 'fake_3': fake_3}

for instr in array_instr:
    num_crates = instr[0]

    from_here = stacks[instr[1]]
    put_here = stacks[instr[2]]
    while num_crates > 0:
        num_crates -= 1
        #get the top crate
        crate = from_here.pop()
        # crate = stacks[instr[1]][-1]

        # add to destination
        put_here.append(crate)


# key, value in dict.items():
stacks_list = []
for k, v in stacks.items():

    last_v = v[-1]

    stacks_list.append(last_v)

print("".join(stacks_list))
