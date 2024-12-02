import re
from tqdm import tqdm

file = open("input.txt", "r")
platform = file.read().split(sep="\n")

total_rows = len(platform)
total_cols = len(platform[0])

prev_platforms = list()


def identical_matrices(A, B):
    return all([a == b for a, b in zip(A, B)])


def tilt_north():
    for col in range(total_cols):
        # rotate the column so north faces east
        rotated_col = ''.join(platform[row][col] for row in range(total_rows - 1, -1, -1))

        # split by # in separate strings, sort the 0 and . and rejoin them
        tilted_col = ''.join(''.join(sorted(x)) for x in re.split(r'(#)', rotated_col))

        for row in range(total_rows - 1, -1, -1):
            platform[row] = platform[row][:col] + tilted_col[total_rows - row - 1] + platform[row][col + 1:]


def tilt_south():
    for col in range(total_cols):
        # rotate the column so south faces east
        rotated_col = ''.join(platform[row][col] for row in range(total_rows))

        # split by # in separate strings, sort the 0 and . and rejoin them
        tilted_col = ''.join(''.join(sorted(x)) for x in re.split(r'(#)', rotated_col))

        for row in range(total_rows):
            platform[row] = platform[row][:col] + tilted_col[row] + platform[row][col + 1:]


def tilt_east():
    for row in range(total_rows):
        # already east so nothing to do
        rotated_row = platform[row]

        # split by # in separate strings, sort the 0 and . and rejoin them
        tilted_row = ''.join(''.join(sorted(x)) for x in re.split(r'(#)', rotated_row))

        platform[row] = tilted_row


def tilt_west():
    for row in range(total_rows):
        # reverse to face east
        rotated_row = platform[row][::-1]

        # split by # in separate strings, sort the 0 and . and rejoin them
        tilted_row = ''.join(''.join(sorted(x)) for x in re.split(r'(#)', rotated_row))

        platform[row] = tilted_row[::-1]


def get_total_load():
    output = 0
    for col in range(total_cols):
        for idx, x in enumerate(''.join(platform[row][col] for row in range(total_rows - 1, -1, -1))):
            if x == 'O':
                output += idx + 1
    return output

break_loop = False

for i in tqdm(range(1000000000)):
    if not break_loop:
        prev_platforms.append([platform[row] for row in range(total_rows)])
        tilt_north()
        tilt_west()
        tilt_south()
        tilt_east()

        for j, prev_platform in enumerate(prev_platforms):
            if identical_matrices(platform, prev_platform):
                loop_cycles = prev_platforms[j:]
                number_of_cycles_before_loop = len(prev_platforms[:j]) - 1 # -1 to ignore original platform
                print(f"There were {number_of_cycles_before_loop} different cycles before the loop began")
                number_of_cycles_in_loop = len(loop_cycles)
                print(f"This loop lasts {number_of_cycles_in_loop} different cycles")

                cycles_to_do = (1000000000 - number_of_cycles_before_loop) % number_of_cycles_in_loop
                platform = loop_cycles[cycles_to_do - 1]
                print(get_total_load())
                break_loop = True
                break
    else:
        break

# for r in range(total_rows):
#     print(platform[r])
