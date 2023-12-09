import math

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

current_nodes = [location for location in location_map.keys() if location[2] == 'A']
steps_taken = []

for current_node in current_nodes:
    steps = 0
    while not current_node[2] == 'Z':
        for direction in instruction:
            if current_node[2] == 'Z':
                break
            else:
                current_node = location_map[current_node][direction_map[direction]]
                steps += 1
    steps_taken.append(steps)

print(math.lcm(*steps_taken))
# This solution really doesn't make sense for the problem, but it works.
