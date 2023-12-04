import sys

file = open("input.txt", "r")
lines_of_text = file.read().split()

output = 0
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def find_first_number(string):
    current_min = sys.maxsize
    first_number = None
    for number, integer in numbers.items():
        index = string.find(number)
        if index < current_min and index != -1:
            current_min = index
            first_number = integer
    counter = 0
    while counter < len(string):
        if string[counter].isdigit() and counter < current_min:
            first_number = int(string[counter])
            break
        counter += 1
    return first_number


def find_last_number(string):
    current_max = -1
    last_number = None
    for number, integer in numbers.items():
        index = string.rfind(number)
        if index > current_max:
            current_max = index
            last_number = integer
    counter = len(string) - 1
    while counter > -1:
        if string[counter].isdigit() and counter > current_max:
            last_number = int(string[counter])
            break
        counter -= 1
    return last_number


for line in lines_of_text:
    calibration_value = find_first_number(line) * 10
    calibration_value += find_last_number(line)

    print(f"Calibration Value found: {calibration_value}")

    output += calibration_value

print(f"Final output: {output}")
