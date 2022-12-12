# with open('day-03-input.txt') as file:
#     lines = [line.strip() for line in file]

def value(letter: str) -> int:
    return (ord(letter) & 31) + 26 * letter.isupper()


def part2(lines: list[str]) -> int:
    GROUP_SIZE = 3
    result = 0
    while lines:
        # a = set(lines.pop())
        # print(a)
        group = [set(lines.pop()) for i in range(GROUP_SIZE)]
        print(group)
        common_letters = set.intersection(*group)
        assert len(common_letters) == 1
        letter = common_letters.pop()
        result += value(letter)
    return result


#
def main():
#     INPUT_FILE_NAME = __file__.replace("solution.py", "input.txt")

    with open('day1-7/day-03-input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    #
    # answer1 = part1(lines)
    # print(answer1)

    answer2 = part2(lines)
    print(answer2)


if __name__ == "__main__":
    main()