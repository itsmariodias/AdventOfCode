file = open("input.txt", "r")
lines_of_text = file.read().split(sep="\n")

red_cubes, green_cubes, blue_cubes = 12, 13, 14
output = 0


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
    games = line.split(":")[1].split(";")
    max_red, max_blue, max_green = 0, 0, 0
    for game in games:
        red, green, blue = get_cube_count(game)
        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue
    output += max_red * max_blue * max_green

print(output)
