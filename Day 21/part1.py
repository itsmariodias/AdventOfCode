file = open("input.txt", "r")
garden = file.read().split(sep="\n")

total_rows = len(garden)
total_cols = len(garden[0])

steps = 64

visited_map = [[False] * total_cols for _ in range(total_rows)]

S_row, S_col = 0, 0

for row in range(total_rows):
    for col in range(total_cols):
        if garden[row][col] == "S":
            S_row, S_col = row, col

stack = [(S_row, S_col, 0)]

garden_plots = set()

while len(stack) > 0:
    row, col, step = stack.pop(0)
    if visited_map[row][col]:
        continue
    visited_map[row][col] = True

    if step % 2 == 0 and step <= steps:
        garden_plots.add((row, col))

    if row > 0:
        if garden[row - 1][col] != "#":
            stack.append((row - 1, col, step + 1))

    if row < total_rows - 1:
        if garden[row + 1][col] != "#":
            stack.append((row + 1, col, step + 1))

    if col > 0:
        if garden[row][col - 1] != "#":
            stack.append((row, col - 1, step + 1))

    if col < total_cols - 1:
        if garden[row][col + 1] != "#":
            stack.append((row, col + 1, step + 1))

print(len(garden_plots))