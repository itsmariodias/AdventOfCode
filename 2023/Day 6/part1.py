file = open("input.txt", "r")
times, distances = file.read().split(sep="\n")

times = [int(x) for x in times.split(':')[1].strip().split()]
distances = [int(x) for x in distances.split(':')[1].strip().split()]
idx = 0
output = 1

while idx < len(times):
    ways = 0
    time = times[idx]
    distance = distances[idx]

    for wait_time in range(time + 1):
        distance_travelled = wait_time * (time - wait_time)
        if distance_travelled > distance:
            ways += 1

    idx += 1
    output *= ways

print(output)