file = open("input.txt", "r")
sequence = file.read().split(sep=",")

output = 0

for string in sequence:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    output += current_value

print(output)
