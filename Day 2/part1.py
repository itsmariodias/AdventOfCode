file = open("input.txt", "r")
lines_of_text = file.read().split(sep="\n")

red_cubes, green_cubes, blue_cubes = 12, 13, 14
output = 0


def get_game_id(string):
    return int(string.split(":")[0].split(" ")[1])


def get_cube_count(game):
    red, green, blue = 0, 0, 0
    for cube in game.strip().split(","):
        count, cube = cube.strip().split()
        count = int(count)
        if cube == 'red':
            red = count
        elif cube == 'green':
            green = count
        elif cube == 'blue':
            blue = count
    return red, green, blue


for line in lines_of_text:
    game_id = get_game_id(line)
    games = line.split(":")[1].split(";")
    possible = True
    for game in games:
        red, green, blue = get_cube_count(game)
        if red > red_cubes or blue > blue_cubes or green > green_cubes:
            possible = False
            break
    if possible:
        output += game_id

print(output)