import re

file = open("input.txt", "r")
platform = file.read().split(sep="\n")

output = 0

total_rows = len(platform)
total_cols = len(platform[0])

for col in range(total_cols):
    # rotate the column so north faces east
    rotated_col = ''.join(platform[row][col] for row in range(total_rows - 1, -1, -1))

    # split by # in separate strings, sort the 0 and . and rejoin them
    tilted_col = ''.join(''.join(sorted(x)) for x in re.split(r'(#)', rotated_col))

    for idx, x in enumerate(tilted_col):
        if x == 'O':
            output += idx + 1

print(output)
