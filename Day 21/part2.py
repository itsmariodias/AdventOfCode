# Get the output for 65, 65 + 131, 65 + 131*2

file = open("input.txt", "r")
garden = file.read().split(sep="\n")

total_rows = len(garden)
total_cols = len(garden[0])

steps = 65

visited_map = set()

S_row, S_col = 0, 0

for row in range(total_rows):
    for col in range(total_cols):
        if garden[row][col] == "S":
            S_row, S_col = row, col

stack = [(S_row, S_col, 0)]

garden_plots = set()

while len(stack) > 0:
    print(len(garden_plots))
    row, col, step = stack.pop(0)
    if (row, col) in visited_map:
        continue
    visited_map.add((row, col))

    if step % 2 == 0 and step <= steps:
        garden_plots.add((row, col))

    if garden[(row - 1) % total_rows][col % total_cols] != "#":
        stack.append((row - 1, col, step + 1))

    if garden[(row + 1) % total_rows][col % total_cols] != "#":
        stack.append((row + 1, col, step + 1))

    if garden[row % total_rows][(col - 1) % total_cols] != "#":
        stack.append((row, col - 1, step + 1))

    if garden[row % total_rows][(col + 1) % total_cols] != "#":
        stack.append((row, col + 1, step + 1))

print(len(garden_plots))

# 65 steps -> 3676 garden plots
# 65 steps -> 32808 garden plots
# 327 steps -> 90974 garden plots
# 458 steps -> 178174 garden plots
