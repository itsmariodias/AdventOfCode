file = open("input.txt", "r")
lines = file.read().split(sep="\n")

output = 0


def permutate(condition_records, group_size, index, current_group_index, current_group_size, permutation):
    # print(f"Now at index {index}")
    if index > len(condition_records) - 1:
        if current_group_index > len(group_size) - 1 or current_group_size == group_size[current_group_index]:
            # print("Got a good record, here is it is")
            # print(permutation)
            permutations.append(permutation)
        return
    if condition_records[index] == '?':
        # print("Mysterious record hmm?")
        condition_records[index] = '.'
        # print(f"Let us assume . at index {index}")
        permutate(condition_records, group_size, index, current_group_index, current_group_size, permutation)
        condition_records[index] = '#'
        # print(f"Let us assume # at index {index}")
        permutate(condition_records, group_size, index, current_group_index, current_group_size, permutation)
        condition_records[index] = '?'
    elif condition_records[index] == '#':
        # print(f"# at index {index}")
        current_group_size += 1
        if current_group_size > group_size[current_group_index]:
            # print("Too many #'s for current group, rejected!")
            # reject this permutation
            return
        # print(f"Adding # at index {index} to our collection...")
        # print(permutation + ['#'])
        permutate(condition_records, group_size, index + 1, current_group_index, current_group_size, permutation + ['#'])
    elif condition_records[index] == '.':
        # print(f". at index {index}")
        if current_group_size == group_size[current_group_index]:
            # print("Well found a good group, lets start finding the new one...")
            # print(permutation + ['.'])
            permutate(condition_records, group_size, index + 1, current_group_index + 1, 0, permutation + ['.'])
        else:
            # print("Found a dot, so can't really do much but continue...")
            permutate(condition_records, group_size, index + 1, current_group_index, current_group_size, permutation + ['.'])


for line in lines:
    condition_records, group_size = line.split()
    condition_records = '?'.join([condition_records] * 5)
    group_size = ','.join([group_size] * 5)
    condition_records = list(condition_records)
    group_size = [int(x) for x in group_size.split(',')]

    # print(condition_records, group_size)
    permutations = list()
    permutate(condition_records, group_size, 0, 0, 0, [])
    print(len(permutations))

    output += len(permutations)

print(output)
