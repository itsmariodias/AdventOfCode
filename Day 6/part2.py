file = open("input.txt", "r")
times, distances = file.read().split(sep="\n")

times = [int(x) for x in times.split(':')[1].strip().split()]
distances = [int(x) for x in distances.split(':')[1].strip().split()]

ways = 0
time = int(''.join(str(x) for x in times))
distance = int(''.join(str(x) for x in distances))

for wait_time in range(time + 1):
    distance_travelled = wait_time * (time - wait_time)
    if distance_travelled > distance:
        ways += 1

print(ways)
