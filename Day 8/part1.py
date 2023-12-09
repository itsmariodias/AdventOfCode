file = open("input.txt", "r")
lines = file.read().split(sep="\n")

location_map = dict()

instruction = lines[0]

direction_map = {'L': 0, 'R': 1}

for line in lines[2:]:
    node = line[0:3]
    left_node = line[7:10]
    right_node = line[12:15]
    location_map[node] = (left_node, right_node)

steps = 0
current_node = 'AAA'

while current_node != 'ZZZ':
    for direction in instruction:
        if current_node == 'ZZZ':
            break
        else:
            current_node = location_map[current_node][direction_map[direction]]
            steps += 1

print(steps)
