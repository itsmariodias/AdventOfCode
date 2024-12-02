from collections import defaultdict

file = open("input.txt", "r")
lines = file.read().split(sep="\n")

height_map = defaultdict(list)
brick_map = defaultdict(dict)

for index, line in enumerate(lines):
    coords1, coords2 = line.split("~")
    x1, y1, z1 = (int(x) for x in coords1.split(","))
    x2, y2, z2 = (int(x) for x in coords2.split(","))

    brick = {"index": index, "x1": x1, "x2": x2, "y1": y1, "y2": y2, "z1": z1, "z2": z2}
    brick_map[index] = brick

for brick in brick_map.values():
    for z in range(brick["z1"], brick["z2"] + 1):
        height_map[z].append(brick["index"])

z = 1

while True:
    bricks = height_map[z].copy()

    for brick_index in bricks:
        while True:


    z += 1