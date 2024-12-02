import sys
import heapq

file = open("input.txt", "r")
pattern_map = file.read().split(sep="\n")

total_rows = len(pattern_map)
total_cols = len(pattern_map[0])

visited_map = [[False] * total_cols for _ in range(total_rows)]
counter = 0

heat_loss_map = [[sys.maxsize] * total_cols for _ in range(total_rows)]
heat_loss_map[0][0] = int(pattern_map[0][0])

direction_map = [[0] * total_cols for _ in range(total_rows)]

min_heap = []

heapq.heappush(min_heap, (heat_loss_map[0][0], 0, 0, '.'))

while counter < total_rows * total_cols and len(min_heap) > 0:
    current_heat_loss, row, col, current_direction = heapq.heappop(min_heap)
    print(row, col)

    if current_direction == '>':
        directions = [(0, 1, '>'), (1, 0, 'v'), (-1, 0, '^')]
    elif current_direction == '<':
        directions = [(0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]
    elif current_direction == '^':
        directions = [(-1, 0, '^'), (0, -1, '<'), (0, 1, '>')]
    elif current_direction == 'v':
        directions = [(1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]
    else:
        directions = [(0, 1, '>'), (1, 0, 'v'), (-1, 0, '^'), (0, -1, '<')]

    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]

        new_direction = direction_map[row][col]
        if direction[2] == current_direction:
            new_direction += 1

        if (-1 < new_row < total_rows and -1 < new_col < total_cols and not visited_map[new_row][new_col]
                and new_direction < 3):
            heat_loss = current_heat_loss + int(pattern_map[new_row][new_col])

            if heat_loss < heat_loss_map[new_row][new_col]:
                heat_loss_map[new_row][new_col] = heat_loss
                heapq.heappush(min_heap, (heat_loss, new_row, new_col, direction[2]))
                direction_map[new_row][new_col] = new_direction

    visited_map[row][col] = True
    counter += 1

print(heat_loss_map[total_rows - 1][total_cols - 1])
