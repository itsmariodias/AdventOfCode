from ast import literal_eval

file = open("input.txt", "r")
dig_plan = file.read().split(sep="\n")

# Start from the center, to prevent issues with negative coordinates
current_row, current_col = 0, 0
vertices = [(current_row, current_col)]

directions = ['R', 'D', 'L', 'U']

for line in dig_plan:
    _, _, color = line.split(sep=' ')

    color = color[1:-1]
    dist = int(literal_eval('0x' + color[1:-1]))

    direction = directions[int(color[-1])]

    if direction == 'U':
        current_row, current_col = current_row, current_col + dist
    elif direction == 'D':
        current_row, current_col = current_row, current_col - dist
    elif direction == 'L':
        current_row, current_col = current_row - dist, current_col
    elif direction == 'R':
        current_row, current_col = current_row + dist, current_col
    vertices.append((current_row, current_col))


# Shoelace formula
def getArea(x1, y1, x2, y2):
    return (x1 * y2) - (y1 * x2)


first_x, first_y = vertices[0]
prev_x, prev_y = first_x, first_y
result = 0
perimeter = 0

for i in range(1, len(vertices)):
    next_x, next_y = vertices[i]
    result = result + getArea(prev_x, prev_y, next_x, next_y)
    # Pick's theorem for the calculating the border (apparently doesn't get covered by Shoelace)
    perimeter += abs(next_x - prev_x + next_y - prev_y)
    prev_x = next_x
    prev_y = next_y

result = abs(result) // 2 + perimeter // 2 + 1

print(result)
