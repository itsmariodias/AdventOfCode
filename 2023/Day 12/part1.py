file = open("input.txt", "r")
lines = file.read().split(sep="\n")

output = 0


def get_group_size(condition_record):
    group_size = []
    size = 0
    for condition in condition_record:
        if condition == '#':
            size += 1
        elif size > 0:
            group_size.append(size)
            size = 0
    if size > 0:
        group_size.append(size)
    return group_size


def permutate(line, group_size, index, permutation):
    global permutations
    if index > len(line) - 1:
        if get_group_size(permutation) == group_size:
            permutations.append(permutation)
        return
    if line[index] == '?':
        permutate(line, group_size, index + 1, permutation + ['.'])
        permutate(line, group_size, index + 1, permutation + ['#'])
    else:
        permutate(line, group_size, index + 1, permutation + [line[index]])


for line in lines:
    condition_records, group_size = line.split()
    condition_records = list(condition_records)
    group_size = [int(x) for x in group_size.split(',')]

    permutations = list()
    permutate(condition_records, group_size, 0, [])
    output += len(permutations)

print(output)