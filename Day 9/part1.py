file = open("input.txt", "r")
lines = file.read().split(sep="\n")

output = 0


def get_difference(numbers):
    differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    if sum(differences) == 0:
        return numbers[0]
    else:
        return numbers[0] - get_difference(differences)


for line in lines:
    numbers = [int(x) for x in line.split()]
    output += get_difference(numbers)

print(output)