file = open("input.txt", "r")
sequence = file.read().split(sep=",")

output = 0

# Since Python 3.7 dict are ordered by insertion, so no need to use OrderedDict
boxes = {x: dict() for x in range(256)}


def get_hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


for string in sequence:
    if '-' in string:
        label = string[:-1]
        hash = get_hash(label)
        if label in boxes[hash].keys():
            boxes[hash].pop(label)
    else:
        focal_length = int(string[-1])
        label = string[:-2]
        hash = get_hash(label)
        boxes[hash][label] = focal_length

for i, box in boxes.items():
    for j, focal_length in enumerate(box.values()):
        output += (i + 1) * (j + 1) * focal_length

print(output)
