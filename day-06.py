with open('day-06-input.txt', 'r') as file:
    dataset = file.read()

# eleven = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
# ten = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

new_list = []
count = 0


start = 0
stop = 4

while True:
    window = dataset[start:stop]
    unique = set(window)
    if len(unique) == 4:
        print(stop)
        break

    start += 1
    stop += 1
    if stop == len(dataset):
        break

# Part 2
