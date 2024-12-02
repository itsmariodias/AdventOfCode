file = open("input.txt", "r")
lines = file.read().split(sep="\n")

output = 0


def diff_by_one(seq1, seq2):
    difference = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            difference += 1
        if difference > 1:
            return False
    return True

def get_vertical_line(pattern, index):
    return ''.join(pattern[r][index] for r in range(len(pattern)))


def check_horizontal_reflection(pattern, total_rows, top_index, bottom_index, smudge_removed):
    if top_index < 0 or bottom_index > total_rows - 1:
        if smudge_removed:
            return True
        else:
            return False
    elif pattern[top_index] == pattern[bottom_index]:
        return check_horizontal_reflection(pattern, total_rows, top_index - 1, bottom_index + 1, smudge_removed)
    else:
        if not smudge_removed:
            if diff_by_one(pattern[top_index], pattern[bottom_index]):
                # If it is possible to get a reflection by changing one pattern, lets try it.
                # print("Found a possibility to smudge")
                return check_horizontal_reflection(pattern, total_rows, top_index - 1, bottom_index + 1, True)
        return False


def check_vertical_reflection(pattern, total_cols, left_index, right_index, smudge_removed):
    if left_index < 0 or right_index > total_cols - 1:
        if smudge_removed:
            return True
        else:
            return False
    elif get_vertical_line(pattern, left_index) == get_vertical_line(pattern, right_index):
        return check_vertical_reflection(pattern, total_cols, left_index - 1, right_index + 1, smudge_removed)
    else:
        if not smudge_removed:
            if diff_by_one(get_vertical_line(pattern, left_index), get_vertical_line(pattern, right_index)):
                # If it is possible to get a reflection by changing one pattern, lets try it.
                # print("Found a possibility to smudge")
                return check_vertical_reflection(pattern, total_cols, left_index - 1, right_index + 1, True)
        return False


def find_reflection(pattern: list):
    total_rows = len(pattern)
    total_cols = len(pattern[0])

    for i in range(total_rows - 1):
        if check_horizontal_reflection(pattern, total_rows, i, i + 1, False):
            # print(f"Horizontal reflection found at {i + 1} and {i + 2}")
            return 100 * (i + 1)

    for i in range(total_cols - 1):
        if check_vertical_reflection(pattern, total_cols, i, i + 1, False):
            # print(f"Vertical reflection found at {i + 1} and {i + 2}")
            return i + 1


i = 0
pattern = []
while i < len(lines):
    if lines[i] == '':
        # print(f"Checking pattern located above line {i+1}")
        output += find_reflection(pattern)
        pattern = []
    else:
        pattern.append(lines[i])
    i += 1

print(output)
