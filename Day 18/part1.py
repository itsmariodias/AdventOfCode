import numpy as np
import skimage
np.set_printoptions(threshold=np.inf)

file = open("input.txt", "r")
dig_plan = file.read().split(sep="\n")


# Start from the center, to prevent issues with negative coordinates
current_row, current_col = 500, 500
vertices = [(current_row, current_col)]

for line in dig_plan:
    direction, dist, color = line.split(sep=' ')
    dist = int(dist)
    if direction == 'U':
        current_row, current_col = current_row - dist, current_col
    elif direction == 'D':
        current_row, current_col = current_row + dist, current_col
    elif direction == 'L':
        current_row, current_col = current_row, current_col - dist
    elif direction == 'R':
        current_row, current_col = current_row, current_col + dist
    vertices.append((current_row, current_col))

total = 0

# Use scikit-image package to create a filled polygon with the given vertices
rows, cols = skimage.draw.polygon(np.array([x[0] for x in vertices]), np.array([x[1] for x in vertices]))
img = np.zeros((1000, 1000), dtype=int)
img[rows, cols] = 1

# Calling sum twice gives us what we need
print(sum(sum(img)))
