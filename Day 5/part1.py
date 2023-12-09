file = open("input.txt", "r")
lines = file.read().split(sep="\n")
seed_map = [int(x) for x in lines[0].split(":")[1].strip().split()]
processed_map = [False] * len(seed_map)

index = 3

for _ in range(7):
    while lines[index] != '':
        destination_start, source_start, range_length = [int(x) for x in lines[index].split()]
        for idx, seed in enumerate(seed_map):
            if source_start <= seed <= source_start + range_length - 1 and not processed_map[idx]:
                seed_map[idx] = seed - source_start + destination_start
                processed_map[idx] = True
        index += 1
    processed_map = [False] * len(seed_map)
    index += 2

print(min(seed_map))
