"""

count: len(set(tuples(x, y))) ->


If the head is ever two steps directly up, down, left, or right from the tail,
the tail must also move one step in that direction so it remains close enough:

Otherwise, if the head and tail aren't touching and aren't in the same row or column,
the tail always moves one step diagonally to keep up:

You just need to work out where the tail goes as the head follows a series of motions.
Assume the head and the tail both start at the same position, overlapping.



"""
with open('day-09-example.txt') as file:
    instructions = [line.strip() for line in file.readlines()]

tails_been_here = []

h_position = (0, 0)

t_position = (0, 0)


for line in instructions:
    list_line = []
    steps = int(line[2])
    direction = line[0]


    if direction == 'R':
        for i in range(1, steps + 1):
            print(f"i: {i}, \t dir: {direction}")

            # Tails follows heads horizontally:
            # Removing bc Y-axis doesn't actually matter:  if h_position[1] == t_position[1]:
            if h_position[0] - t_position[0] == 1:

                t_position = h_position
                h_position = (h_position[0] + 1, h_position[1])
                tails_been_here.append(t_position)

                print(f"  ==tails follows heads==")
                print(f"  new h_position: {h_position} \t new t_position: {t_position}")

            else:
                h_position = (h_position[0] + 1, h_position[1])


            # if abs(h_position[1] - t_position[1]) <= 1:
            #
            #         h_position = (h_position[0] + 1, h_position[0])
            #         print(f"  ==tails doesn't move==")
            #         print(f"  new h_position: {h_position} \t new t_position: {t_position}")
            #     if abs(h_position[1] - t_position[1]) > 1:
            #         h_position = (h_position[0] + 1, h_position[0])
            #         t_position = h_position
            #         tails_been_here.append(t_position)
            #         print(f"  ==tails moves diagonally==")
            #         print(f"  new h_position: {h_position} \t new t_position: {t_position}")


    if direction == 'U':
        if h_position[1] - t_position[1] == 1:

            t_position = h_position
            h_position = (h_position[0], h_position[1] + 1)
            tails_been_here.append(t_position)

            print(f"  ==tails follows heads==")
            print(f"  new h_position: {h_position} \t new t_position: {t_position}")

        else:
            h_position = (h_position[0], h_position[1] + 1)


    if direction == 'L':
        for i in range(1, steps + 1):
            print(f"i: {i}, \t dir: {direction}")

            if h_position[0] - t_position[0] == -1:

                t_position = h_position
                h_position = (h_position[0] - 1, h_position[1])
                tails_been_here.append(t_position)

                print(f"  ==tails follows heads==")
                print(f"  new h_position: {h_position} \t new t_position: {t_position}")

            else:
                h_position = (h_position[0] - 1, h_position[1])

    if direction == 'D':
        for i in range(1, steps + 1):
            print(f"i: {i}, \t dir: {direction}")
            # Tails follows heads
            if h_position[0] == t_position[0]:
                h_position = (h_position[0], h_position[1] - 1)
                t_position = (t_position[0], t_position[1] - 1)
                tails_been_here.append(t_position)
                print(f"  ==tails follows heads==")
                print(f"  new h_position: {h_position} \t new t_position: {t_position}")

            # Tail stays in place or moves to head's old position
            if h_position[0] != t_position[0]:

                if abs(h_position[0] - t_position[0]) <= 1:
                    h_position = (h_position[0], h_position[1] - 1)
                    print(f"  ==tails doesn't move==")
                    print(f"  new h_position: {h_position} \t new t_position: {t_position}")
                if abs(h_position[1] - t_position[1]) > 1:
                    h_position = (h_position[0], h_position[1] - 1)
                    t_position = h_position
                    tails_been_here.append(t_position)
                    print(f"  ==tails moves diagonally==")
                    print(f"  new h_position: {h_position} \t new t_position: {t_position}")



print(len(set(tails_been_here)))

