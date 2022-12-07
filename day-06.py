with open('day-06-input.txt', 'r') as file:
    dataset = file.read()

# eleven = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
# ten = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

new_list = []
count = 0


start = 0
stop = 4

# Part 1
# while True:
#     window = dataset[start:stop]
#     unique = set(window)
#     if len(unique) == 4:
#         print(stop)
#         break
#
#     start += 1
#     stop += 1
#     if stop == len(dataset):
#         break

# Part 2
stop_2 = 14
nineteen = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

while True:
    window = dataset[start:stop_2]
    unique = set(window)
    if len(unique) == 14:
        print(stop_2)
        break

    start += 1
    stop_2 += 1
    if stop_2 == len(dataset):
        break
