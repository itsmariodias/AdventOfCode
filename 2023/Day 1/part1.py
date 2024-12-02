file = open("input.txt", "r")
lines_of_text = file.read().split()

output = 0

for line in lines_of_text:
    calibration_value = 0
    counter = 0
    while counter < len(line):
        if line[counter].isdigit():
            calibration_value = int(line[counter]) * 10
            break
        counter += 1

    counter = len(line) - 1
    while counter > -1:
        if line[counter].isdigit():
            calibration_value += int(line[counter])
            break
        counter -= 1

    print(f"Calibration Value found: {calibration_value}")

    output += calibration_value

print(f"Final output: {output}")