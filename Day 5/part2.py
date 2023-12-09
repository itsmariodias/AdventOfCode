file = open("input.txt", "r")
lines = file.read().split(sep="\n")

# Get the seed ranges
seeds = [int(x) for x in lines[0].split(":")[1].strip().split()]
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_start, range_length = seeds[i], seeds[i + 1]
    seed_ranges.append((seed_start, seed_start + range_length - 1))
seed_ranges.sort(key=lambda x: x[0])
print(seed_ranges)


def get_y_ranges(index, x_ranges):
    index += 2
    # Get the x to y ranges
    x_to_y_ranges = []
    x_to_y_map = dict()
    while lines[index] != '':
        destination_start, source_start, range_length = [int(x) for x in lines[index].split()]
        x_to_y_map[source_start] = destination_start
        x_to_y_ranges.append((source_start, source_start + range_length - 1))
        index += 1
    x_to_y_ranges.sort(key=lambda x: x[0])

    # Get the y ranges
    i = 0
    while i < len(x_ranges):
        x_start, x_end = x_ranges[i]
        for x_to_y in x_to_y_ranges:
            x_to_y_start, x_to_y_end = x_to_y
            if x_to_y_start <= x_start <= x_end <= x_to_y_end:
                y_start = x_to_y_map[x_to_y_start] + x_start - x_to_y_start
                y_end = x_to_y_map[x_to_y_start] + x_end - x_to_y_start
                x_ranges[i] = (y_start, y_end)
                break
            elif x_start < x_to_y_start <= x_end <= x_to_y_end:
                y_start = x_to_y_map[x_to_y_start]
                y_end = x_to_y_map[x_to_y_start] + x_end - x_to_y_start
                x_ranges[i] = (y_start, y_end)
                x_ranges.insert(i, (x_start, x_to_y_start - 1))
                i += 1
                break
            elif x_to_y_start <= x_start <= x_to_y_end < x_end:
                y_start = x_to_y_map[x_to_y_start] + x_start - x_to_y_start
                y_end = x_to_y_map[x_to_y_start] + x_to_y_end - x_to_y_start
                x_ranges[i] = (y_start, y_end)
                x_ranges.insert(i + 1, (x_to_y_end + 1, x_end))
                break
            elif x_start < x_to_y_start <= x_to_y_end < x_end:
                y_start = x_to_y_map[x_to_y_start]
                y_end = x_to_y_map[x_to_y_start] + x_to_y_end - x_to_y_start
                x_ranges.insert(i, (x_start, x_to_y_start - 1))
                i += 1
                x_ranges[i] = (y_start, y_end)
                x_ranges.insert(i + 1, (x_to_y_end + 1, x_end))
                break
        i += 1
    x_ranges.sort(key=lambda x: x[0])
    print(x_ranges)
    return index, x_ranges


index, soil_ranges = get_y_ranges(1, seed_ranges)
index, fertilizer_ranges = get_y_ranges(index, soil_ranges)
index, water_ranges = get_y_ranges(index, fertilizer_ranges)
index, light_ranges = get_y_ranges(index, water_ranges)
index, temperature_ranges = get_y_ranges(index, light_ranges)
index, humidity_ranges = get_y_ranges(index, temperature_ranges)
index, location_ranges = get_y_ranges(index, humidity_ranges)

print(min(x[0] for x in location_ranges))
