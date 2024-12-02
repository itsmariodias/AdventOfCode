file = open("input.txt", "r")
image = file.read().split(sep="\n")

total_rows = len(image)
total_cols = len(image[0])

empty_row_indexes = []
# step 1, find all rows with no galaxies
for row in range(total_rows):
    is_empty = True
    for i in range(total_cols):
        if image[row][i] == '#':
            is_empty = False
    if is_empty:
        empty_row_indexes.append(row)

empty_column_indexes = []
# step 2, find all columns with no galaxies
for col in range(total_cols):
    is_empty = True
    for i in range(total_rows):
        if image[i][col] == '#':
            is_empty = False
            break
    if is_empty:
        empty_column_indexes.append(col)

galaxy_coordinates = []
for r in range(total_rows):
    for c in range(total_cols):
        if image[r][c] == '#':
            galaxy_coordinates.append((r, c))

total_sum = 0
for i in range(len(galaxy_coordinates)):
    x1, y1 = galaxy_coordinates[i]
    for j in range(i + 1, len(galaxy_coordinates)):
        x2, y2 = galaxy_coordinates[j]
        manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
        # print(f'Galaxy {i + 1} and Galaxy {j + 1}: {manhattan_dist}')
        for row in empty_row_indexes:
            if x1 < row < x2 or x2 < row < x2:
                manhattan_dist += 1000000 - 1
        for col in empty_column_indexes:
            if y1 < col < y2 or y2 < col < y1:
                manhattan_dist += 1000000 - 1
        # print(f'Galaxy {i+1} and Galaxy {j+1}: {manhattan_dist}')
        total_sum += manhattan_dist

print(total_sum)
