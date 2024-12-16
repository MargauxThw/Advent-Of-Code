f = open("input.txt", "r")
text = f.read().splitlines()

def get_gps(y, x):
    return 100 * y + x

def get_double(char):
    if char == "#":
        return "##"
    if char == ".":
        return ".."
    if char == "O":
        return "[]"
    return char + "."


def get_impacted(dir, map, robot):
    to_move = []
    valid = True
        
    def get_to_move(y, x):
        nonlocal valid
        if not valid:
            return
        if map[y + dir][x] == "[":
            if map[y + (dir * 2)][x] == "#" or map[y + (dir * 2)][x + 1] == "#":
                valid = False
                return
            if map[y + dir][x] not in to_move:
                to_move.append([y + dir, x, "["])
                get_to_move(y + dir, x)
            if map[y + dir][x + 1] not in to_move:
                to_move.append([y + dir, x + 1, "]"])
                get_to_move(y + dir, x + 1)
                
        elif map[y + dir][x] == "]":
            if map[y + (dir * 2)][x] == "#" or map[y + (dir * 2)][x - 1] == "#":
                valid = False
                return
            if map[y + dir][x] not in to_move:
                to_move.append([y + dir, x, "]"])
                get_to_move(y + dir, x)
            if map[y + dir][x - 1] not in to_move:
                to_move.append([y + dir, x - 1, "["])
                get_to_move(y + dir, x - 1)
    
    get_to_move(robot[0], robot[1])
    if not valid:
        return robot
    
    if map[robot[0] + dir][robot[1]] == "[":
        map[robot[0] + dir][robot[1] + 1] = "."
    elif map[robot[0] + dir][robot[1]] == "]":
        map[robot[0] + dir][robot[1] - 1] = "."
    
    map[robot[0] + dir][robot[1]] = "@"
    
    for i in range(len(to_move)):
        map[to_move[i][0] + dir][to_move[i][1]] = to_move[i][2]
        if [to_move[i][0] - dir, to_move[i][1], "]"] not in to_move and [to_move[i][0] - dir, to_move[i][1], "["] not in to_move:
            if dir == -1 and to_move[i][0] - dir < y:
                map[to_move[i][0]][to_move[i][1]] = "."
            elif dir == 1 and to_move[i][0] - dir > y:
                map[to_move[i][0]][to_move[i][1]] = "."
    
    map[robot[0]][robot[1]] = "."
    return [robot[0] + dir,robot[1]]

map = []
moves = []
robot = [0, 0]
map_mode = True
for line in text:
    if line == "":
        map_mode = False
    elif map_mode:
        map.append([new_l for new_l in "".join([get_double(l) for l in line])])
        if "@" in line:
            robot = [len(map) - 1, map[len(map) - 1].index("@")]
    else: 
        moves.extend(line)


for move in moves:
    # print("MOVE:", move)
    # print("ROBOT:", robot, map[robot[0]][robot[1]])
    y, x = robot[0], robot[1]
    if move == "^":
        above = [y - 1, x]
        if map[above[0]][above[1]] == ".":
            map[y][x] = "."
            map[above[0]][above[1]] = "@"
            robot = above
        elif map[above[0]][above[1]] in "[]":
            robot = get_impacted(-1, map, robot)
    
    elif move == ">":
        right = [y, x + 1]
        if map[right[0]][right[1]] == ".":
            map[y][x] = "."
            map[right[0]][right[1]] = "@"
            robot = right
        elif map[right[0]][right[1]] == "[":
            if right[1] < len(map[y]) - 1 and map[right[0]][right[1] + 2] != "#":
                if map[right[0]][right[1] + 2] == "[":
                    temp_x = right[1] + 2
                    while temp_x < len(map[y]) - 1 and map[right[0]][temp_x] != "#":
                        if map[right[0]][temp_x] == ".":
                            # map[right[0]][temp_x] = "O"
                            for i in range(right[1], temp_x + 1):
                                next = map[right[0]][i]
                                if next == "." or next == "[":
                                    map[right[0]][i] = "]"
                                elif next == "]":
                                    map[right[0]][i] = "["
                                    
                            map[y][x] = "."
                            map[right[0]][right[1]] = "@"
                            robot = right
                            break
                        temp_x += 1
                else:
                    map[right[0]][right[1] + 1] = "["
                    map[right[0]][right[1] + 2] = "]"
                    map[y][x] = "."
                    map[right[0]][right[1]] = "@"
                    robot = right
                    
    elif move == "v":
        below = [y + 1, x]
        if map[below[0]][below[1]] == ".":
            map[y][x] = "."
            map[below[0]][below[1]] = "@"
            robot = below
        elif map[below[0]][below[1]] in "[]":
            robot = get_impacted(1, map, robot)
    
    elif move == "<":
        left = [y, x - 1]
        if map[left[0]][left[1]] == ".":
            map[y][x] = "."
            map[left[0]][left[1]] = "@"
            robot = left
        elif map[left[0]][left[1]] == "]":
            if left[1] > 0 and map[left[0]][left[1] - 2] != "#":
                if map[left[0]][left[1] - 2] == "]":
                    temp_x = left[1] - 2
                    while temp_x > 0 and map[left[0]][temp_x] != "#":
                        if map[left[0]][temp_x] == ".":
                            for i in range(left[1], temp_x - 1 , -1):
                                next = map[left[0]][i]
                                if next == "." or next == "]":
                                    map[left[0]][i] = "["
                                elif next == "[":
                                    map[left[0]][i] = "]"
                            map[y][x] = "."
                            map[left[0]][left[1]] = "@"
                            robot = left
                            break
                        temp_x -= 1
                else:
                    map[left[0]][left[1] - 1] = "]"
                    map[left[0]][left[1] - 2] = "["
                    map[y][x] = "."
                    map[left[0]][left[1]] = "@"
                    robot = left
    
    # for row in map:
    #     print("".join(row))
    
    
sum = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "[":
            sum += get_gps(y, x)

print(sum)
