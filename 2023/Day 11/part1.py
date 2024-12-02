import copy

file = open("input.txt", "r")
lines = file.read().split(sep="\n")

total_rows = len(lines)
total_cols = len(lines[0])

image = []

# step 1, find all rows with no galaxies
for row in range(total_rows):
    is_empty = True
    for i in range(total_cols):
        if lines[row][i] == '#':
            is_empty = False
    if is_empty:
        image.append(list(lines[row]))
    image.append(list(lines[row]))

total_rows = len(image)

new_image = copy.deepcopy(image)

offset = 0
# step 2, find all columns with no galaxies
for col in range(total_cols):
    is_empty = True
    for i in range(total_rows):
        if image[i][col] == '#':
            is_empty = False
            break
    if is_empty:
        for i in range(total_rows):
            new_image[i].insert(col + offset, '.')
        offset += 1

total_cols = len(new_image[0])

galaxy_coordinates = []
for r in range(total_rows):
    string = ''
    for c in range(total_cols):
        if new_image[r][c] == '#':
            galaxy_coordinates.append((r, c))
        string += str(new_image[r][c])
    # print(string)

image = new_image

total_sum = 0

for i in range(len(galaxy_coordinates)):
    x1, y1 = galaxy_coordinates[i]
    for j in range(i + 1, len(galaxy_coordinates)):
        x2, y2 = galaxy_coordinates[j]
        manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
        # print(f'Galaxy {i+1} and Galaxy {j+1}: {manhattan_dist}')
        total_sum += manhattan_dist

print(total_sum)
