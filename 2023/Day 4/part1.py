import math

file = open("input.txt", "r")
cards = file.read().split(sep="\n")

output = 0

for card in cards:
    numbers = card.split(":")[1]
    winning_numbers = numbers.split("|")[0].strip().split()
    your_numbers = numbers.split("|")[1].strip().split()

    points = -1
    for number in your_numbers:
        if number in winning_numbers:
            points += 1
    if points != -1:
        output += int(math.pow(2, points))

print(output)
