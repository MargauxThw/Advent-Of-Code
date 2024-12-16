f = open("input.txt", "r")
text = f.read().splitlines()

def get_gps(y, x):
    return 100 * y + x

map = []
moves = []
robot = [0, 0]
map_mode = True
for line in text:
    if line == "":
        map_mode = False
    elif map_mode:
        map.append([l for l in line])
        if "@" in line:
            robot = [len(map) - 1, line.index("@")]
    else: 
        moves.extend(line)

for move in moves:
    # print("MOVE:", move)
    y, x = robot[0], robot[1]
    if move == "^":
        above = [y - 1, x]
        if map[above[0]][above[1]] == ".":
            map[y][x] = "."
            map[above[0]][above[1]] = "@"
            robot = above
        elif map[above[0]][above[1]] == "O":
            if above[0] > 0 and map[above[0] - 1][above[1]] != "#":
                if map[above[0] - 1][above[1]] == "O":
                    temp_y = above[0] - 1
                    while temp_y > 0 and map[temp_y][above[1]] != "#":
                        if map[temp_y][above[1]] == ".":
                            map[temp_y][above[1]] = "O"
                            map[y][x] = "."
                            map[above[0]][above[1]] = "@"
                            robot = above
                            break
                        temp_y -= 1
                else:
                    map[above[0] - 1][above[1]] = "O"
                    map[y][x] = "."
                    map[above[0]][above[1]] = "@"
                    robot = above
                    
    elif move == ">":
        right = [y, x + 1]
        if map[right[0]][right[1]] == ".":
            map[y][x] = "."
            map[right[0]][right[1]] = "@"
            robot = right
        elif map[right[0]][right[1]] == "O":
            if right[1] < len(map[y]) - 1 and map[right[0]][right[1] + 1] != "#":
                if map[right[0]][right[1] + 1] == "O":
                    temp_x = right[1] + 1
                    while temp_x < len(map[y]) - 1 and map[right[0]][temp_x] != "#":
                        if map[right[0]][temp_x] == ".":
                            map[right[0]][temp_x] = "O"
                            map[y][x] = "."
                            map[right[0]][right[1]] = "@"
                            robot = right
                            break
                        temp_x += 1
                else:
                    map[right[0]][right[1] + 1] = "O"
                    map[y][x] = "."
                    map[right[0]][right[1]] = "@"
                    robot = right
                    
    elif move == "v":
        below = [y + 1, x]
        if map[below[0]][below[1]] == ".":
            map[y][x] = "."
            map[below[0]][below[1]] = "@"
            robot = below
        elif map[below[0]][below[1]] == "O":
            if below[0] < len(map) - 1 and map[below[0] + 1][below[1]] != "#":
                if map[below[0] + 1][below[1]] == "O":
                    temp_y = below[0] + 1
                    while temp_y < len(map) - 1 and map[temp_y][below[1]] != "#":
                        if map[temp_y][below[1]] == ".":
                            map[temp_y][below[1]] = "O"
                            map[y][x] = "."
                            map[below[0]][below[1]] = "@"
                            robot = below
                            break
                        temp_y += 1
                else:
                    map[below[0] + 1][below[1]] = "O"
                    map[y][x] = "."
                    map[below[0]][below[1]] = "@"
                    robot = below
                    
    elif move == "<":
        left = [y, x - 1]
        if map[left[0]][left[1]] == ".":
            map[y][x] = "."
            map[left[0]][left[1]] = "@"
            robot = left
        elif map[left[0]][left[1]] == "O":
            if left[1] > 0 and map[left[0]][left[1] - 1] != "#":
                if map[left[0]][left[1] - 1] == "O":
                    temp_x = left[1] - 2
                    while temp_x > 0 and map[left[0]][temp_x] != "#":
                        if map[left[0]][temp_x] == ".":
                            map[left[0]][temp_x] = "O"
                            map[y][x] = "."
                            map[left[0]][left[1]] = "@"
                            robot = left
                            break
                        temp_x -= 1
                else:
                    map[left[0]][left[1] - 1] = "O"
                    map[y][x] = "."
                    map[left[0]][left[1]] = "@"
                    robot = left
    
    # for row in map:
    #     print("".join(row))
    
sum = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "O":
            sum += get_gps(y, x)

print(sum)