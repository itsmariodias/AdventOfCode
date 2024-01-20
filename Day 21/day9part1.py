from tqdm import tqdm

# Using the Day 9 part 1 code to extrapolate the answer for the next set of steps until we reach 202300 * 131 + 65 steps

file = open("extrapolation.txt", "r")
lines = file.read().split(sep="\n")

output = 0


def get_difference(numbers):
    differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    if sum(differences) == 0:
        return numbers[-1] + 0
    else:
        return numbers[-1] + get_difference(differences)


numbers = [int(x) for x in lines[0].split()]

for _ in tqdm(range(202300 - 2)):
    numbers.append(get_difference(numbers[-3:])) # you only the last 3 sets to extrapolate the next one

print(numbers[-1])
