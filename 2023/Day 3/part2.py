import math

file = open("input.txt", "r")
schematic = file.read().split(sep="\n")

output = 0

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '+', '=', '-', '_', '~', '`', '(', ')', '{', '}', '[', ']', '|',
           '\\', '\'', '\"', ':', ';', '<', '>', ',', '/']

total_rows = len(schematic)
total_columns = len(schematic[0])


def get_full_number(row, col):
    number = int(schematic[row][col])
    c = col - 1
    while c > -1 and schematic[row][c].isdigit():
        number += int(schematic[row][c]) * math.pow(10, col - c)
        c -= 1
    c = col + 1
    while c < total_columns and schematic[row][c].isdigit():
        number = int(schematic[row][c]) + number * 10
        c += 1
    return int(number)


def check_adjacent_areas(row, col):
    number_count = 0
    numbers = []

    top, bottom = False, False

    # check left
    if col > 0:
        if schematic[row][col - 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row, col - 1))
            number_count += 1
    # check right
    if col < total_columns - 1:
        if schematic[row][col + 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row, col + 1))
            number_count += 1
    # check top
    if row > 0:
        if schematic[row - 1][col].isdigit() and number_count < 3:
            numbers.append(get_full_number(row - 1, col))
            number_count += 1
            top = True
    # check bottom
    if row < total_rows - 1:
        if schematic[row + 1][col].isdigit() and number_count < 3:
            numbers.append(get_full_number(row + 1, col))
            number_count += 1
            bottom = True
    # check upper left
    if row > 0 and col > 0 and not top:
        if schematic[row - 1][col - 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row - 1, col - 1))
            number_count += 1
    # check upper right
    if row > 0 and col < total_columns - 1 and not top:
        if schematic[row - 1][col + 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row - 1, col + 1))
            number_count += 1
    # check bottom left
    if row < total_rows - 1 and col > 0 and not bottom:
        if schematic[row + 1][col - 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row + 1, col - 1))
            number_count += 1
    # check bottom right
    if row < total_rows - 1 and col < total_columns - 1 and not bottom:
        if schematic[row + 1][col + 1].isdigit() and number_count < 3:
            numbers.append(get_full_number(row + 1, col + 1))
            number_count += 1
    if number_count in [0, 1, 3]:
        return -1, -1
    else:
        return numbers[0], numbers[1]


for row in range(total_rows):
    for col in range(total_columns):
        if schematic[row][col] == "*":
            number1, number2 = check_adjacent_areas(row, col)
            print(number1, number2)
            if number1 != -1 and number2 != -1:
                output += number1 * number2

print(output)
