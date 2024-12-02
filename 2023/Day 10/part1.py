file = open("input.txt", "r")
maze = file.read().split(sep="\n")

total_rows = len(maze)
total_cols = len(maze[0])

travelled = [[0] * total_cols for _ in range(total_rows)]

S_row, S_col = 0, 0

# find S's location
for row in range(total_rows):
    for col in range(total_cols):
        if maze[row][col] == 'S':
            S_row, S_col = row, col
            break

farthest = 0

print(f"Found S's location at ({S_row},{S_col})")

north_pipes = ['|', 'L', 'J']
south_pipes = ['|', '7', 'F']
east_pipes = ['-', 'L', 'F']
west_pipes = ['-', 'J', '7']


def travel(stack):
    while len(stack) > 0:
        r, c, incoming_direction, steps = stack.pop()
        global farthest

        # Add the step to map if not yet come here, else skip if a better route was found
        if 0 < travelled[r][c] < steps + 1:
            return
        elif travelled[r][c] == 0:
            travelled[r][c] = steps + 1
        else:
            travelled[r][c] = min(travelled[r][c], steps + 1)

        # Determine the next direction to move towards
        if maze[r][c] == '|':
            if incoming_direction == 'south' and r > 0 and maze[r - 1][c] in south_pipes:
                stack.append((r - 1, c, incoming_direction, steps + 1))
            elif incoming_direction == 'north' and r < total_rows - 1 and maze[r + 1][c] in north_pipes:
                stack.append((r + 1, c, incoming_direction, steps + 1))
        elif maze[r][c] == '-':
            if incoming_direction == 'east' and c > 0 and maze[r][c - 1] in east_pipes:
                stack.append((r, c - 1, incoming_direction, steps + 1))
            elif incoming_direction == 'west' and c < total_cols - 1 and maze[r][c + 1] in west_pipes:
                stack.append((r, c + 1, incoming_direction, steps + 1))
        elif maze[r][c] == 'L':
            if incoming_direction == 'north' and c < total_cols - 1 and maze[r][c + 1] in west_pipes:
                stack.append((r, c + 1, 'west', steps + 1))
            elif incoming_direction == 'east' and r > 0 and maze[r - 1][c] in south_pipes:
                stack.append((r - 1, c, 'south', steps + 1))
        elif maze[r][c] == 'J':
            if incoming_direction == 'north' and c > 0 and maze[r][c - 1] in east_pipes:
                stack.append((r, c - 1, 'east', steps + 1))
            elif incoming_direction == 'west' and r > 0 and maze[r - 1][c] in south_pipes:
                stack.append((r - 1, c, 'south', steps + 1))
        elif maze[r][c] == '7':
            if incoming_direction == 'south' and c > 0 and maze[r][c - 1] in east_pipes:
                stack.append((r, c - 1, 'east', steps + 1))
            elif incoming_direction == 'west' and r < total_rows - 1 and maze[r + 1][c] in north_pipes:
                stack.append((r + 1, c, 'north', steps + 1))
        elif maze[r][c] == 'F':
            if incoming_direction == 'south' and c < total_cols - 1 and maze[r][c + 1] in west_pipes:
                stack.append((r, c + 1, 'west', steps + 1))
            elif incoming_direction == 'east' and r < total_rows - 1 and maze[r + 1][c] in north_pipes:
                stack.append((r + 1, c, 'north', steps + 1))


if S_row > 0 and maze[S_row - 1][S_col] in south_pipes:
    travel([(S_row - 1, S_col, 'south', 0)])
if S_row < total_rows - 1 and maze[S_row + 1][S_col] in north_pipes:
    travel([(S_row + 1, S_col, 'north', 0)])
if S_col > 0 and maze[S_row][S_col - 1] in east_pipes:
    travel([(S_row, S_col - 1, 'east', 0)])
if S_col < total_cols - 1 and maze[S_row][S_col + 1] in west_pipes:
    travel([(S_row, S_col + 1, 'west', 0)])

print(f"Farthest step is {farthest}")
