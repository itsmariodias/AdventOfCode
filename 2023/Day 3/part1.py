file = open("input.txt", "r")
schematic = file.read().split(sep="\n")

output = 0

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '+', '=', '-', '_', '~', '`', '(', ')', '{', '}', '[', ']', '|',
           '\\', '\'', '\"', ':', ';', '<', '>', ',', '/']

total_rows = len(schematic)
total_columns = len(schematic[0])


def check_adjacent_areas(row, col):
    # check left
    if col > 0:
        if schematic[row][col - 1] in symbols:
            return True
    # check right
    if col < total_columns - 1:
        if schematic[row][col + 1] in symbols:
            return True
    # check top
    if row > 0:
        if schematic[row - 1][col] in symbols:
            return True
    # check bottom
    if row < total_rows - 1:
        if schematic[row + 1][col] in symbols:
            return True
    # check upper left
    if row > 0 and col > 0:
        if schematic[row - 1][col - 1] in symbols:
            return True
    # check upper right
    if row > 0 and col < total_columns - 1:
        if schematic[row - 1][col + 1] in symbols:
            return True
    # check bottom left
    if row < total_rows - 1 and col > 0:
        if schematic[row + 1][col - 1] in symbols:
            return True
    # check bottom right
    if row < total_rows - 1 and col < total_columns - 1:
        if schematic[row + 1][col + 1] in symbols:
            return True
    return False


for row in range(total_rows):
    scanner = ''
    is_part_number = False
    for col in range(total_columns):
        if schematic[row][col].isdigit():
            scanner += schematic[row][col]
            is_part_number = is_part_number or check_adjacent_areas(row, col)
        if schematic[row][col] == '.' or schematic[row][col] in symbols or col == total_columns - 1:
            if is_part_number and scanner != '':
                print(scanner)
                output += int(scanner)
            scanner = ''
            is_part_number = False

print(output)
