# Begin Part 2:

with open('day-09-pt2-input.txt') as file:
    instructions = [line.strip() for line in file.readlines()]

knots_been_here = []


knots = [(0, 0)] * 10
print(knots)


def print_knot_positions(k):

    grid = [['.' for x in range(20)] for y in range(20)]
    for index, (x, y) in enumerate(k):
        grid[y][x] = str(index)
    for x in reversed(grid):
        print(''.join(x))


def move(lead_, follow):

    delta_x = lead_[0] - follow[0]
    delta_y = lead_[1] - follow[1]
    vector = (delta_x, delta_y)


    if abs(delta_x) < 2 and abs(delta_y) < 2:
        return follow

    def clamp(n, low, high):
        return min(max(low, n), high)

    move_x = clamp(delta_x, -1, 1)
    move_y = clamp(delta_y, -1, 1)

    return follow[0] + move_x, follow[1] + move_y






    # # KNOTS[1] only moves up if KNOTS[0] - KNOTS[1] == 2:
    # if knots[0][1] - knots[1][1] == 2:
    #     knots[1] = (knots[1][0] + 1, knots[1][1] + 1)
    #
    # if knots[0][1] - knots[1][1] == 0:
    #     pass
    # if knots[0][1] - knots[1][1] < 0:
    #     knots[1] = (knots[1][0] + 1, knots[1][1] - 1)
    #
    # for i, knot in enumerate(knots[2:-1]):
    # return 0, 0  # follows new position as tuple


knot_locations = set()

for line in instructions:
    split_line = line.split()

    steps = int(split_line[1])
    direction = line[0]
    # print(f"==Going {steps} steps in {direction} direction:==")

    for s in range(1, steps + 1):
        if direction == 'R':
            knots[0] = (knots[0][0] + 1, knots[0][1])

        elif direction == 'U':
            knots[0] = (knots[0][0], knots[0][1]+1)

        elif direction == 'L':
            knots[0] = (knots[0][0]-1, knots[0][1])

        elif direction == 'D':
            knots[0] = (knots[0][0], knots[0][1]-1)


        for i in range(len(knots)-1):
            knots[i+1] = move(knots[i], knots[i+1])

        knot_locations.add(knots[-1])


print(len(knot_locations))
