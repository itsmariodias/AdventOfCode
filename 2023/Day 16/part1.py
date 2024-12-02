file = open("input.txt", "r")
contraption = file.read().split(sep="\n")

total_rows = len(contraption)
total_cols = len(contraption[0])

energy_map = [[False] * total_cols for _ in range(total_rows)]

direction_energy_map = set()

stack = [('>', 0, 0)]


def left(row, col):
    cell = contraption[row][col]
    if cell == '|':
        return [('^', row - 1, col), ('v', row + 1, col)]
    elif cell == '/':
        return [('^', row - 1, col)]
    elif cell == '\\':
        return [('v', row + 1, col)]
    else:
        return [('>', row, col + 1)]


def right(row, col):
    cell = contraption[row][col]
    if cell == '|':
        return [('^', row - 1, col), ('v', row + 1, col)]
    elif cell == '/':
        return [('v', row + 1, col)]
    elif cell == '\\':
        return [('^', row - 1, col)]
    else:
        return [('<', row, col - 1)]


def up(row, col):
    cell = contraption[row][col]
    if cell == '-':
        return [('<', row, col - 1), ('>', row, col + 1)]
    elif cell == '/':
        return [('>', row, col + 1)]
    elif cell == '\\':
        return [('<', row, col - 1)]
    else:
        return [('^', row - 1, col)]


def down(row, col):
    cell = contraption[row][col]
    if cell == '-':
        return [('<', row, col - 1), ('>', row, col + 1)]
    elif cell == '/':
        return [('<', row, col - 1)]
    elif cell == '\\':
        return [('>', row, col + 1)]
    else:
        return [('v', row + 1, col)]


while len(stack) > 0:
    direction, row, col = stack.pop()
    if 0 <= row < total_rows and 0 <= col < total_cols and (direction, row, col) not in direction_energy_map:
        energy_map[row][col] = True
        direction_energy_map.add((direction, row, col))
        if direction == '>':
            stack.extend(left(row, col))
        elif direction == '<':
            stack.extend(right(row, col))
        elif direction == '^':
            stack.extend(up(row, col))
        elif direction == 'v':
            stack.extend(down(row, col))

# for r in range(total_rows):
#     string = ""
#     for c in range(total_cols):
#         string += '#' if energy_map[r][c] else '.'
#     print(string)

print(sum([sum(row) for row in energy_map]))
