f = open("input.txt", "r")
str_rows = f.read().splitlines()

rows = []
total_removals = 0
total_possible_removals = 0
for y in range(len(str_rows)):
    rows.append([])
    for x in range(len(str_rows[0])):
        rows[y].append(str_rows[y][x])
        if str_rows[y][x] == "@":
            total_possible_removals += 1

def check(y, x):
    dots = 0
    # Find 5 dots or empty spaces in this
    # [y-1][x-1] | [y-1][x] | [y-1][x+1]
    #  [y][x-1]  |     @    |  [y][x+1]
    # [y+1][x-1] | [y+1][x] | [y+1][x+1]
    above = y - 1
    below = y + 1
    left = x - 1
    right = x + 1
    
    if above < 0:
        dots += 3
    else: 
        if left < 0 or rows[above][left] == ".":
            dots += 1
        if rows[above][x] == ".":
            dots += 1
        if right == len(rows[0]) or rows[above][right] == ".":
            dots += 1

    if left < 0 or rows[y][left] == ".":
        dots += 1

    if right == len(rows[0]) or rows[y][right] == ".":
        dots += 1

    if below == len(rows):
        dots += 3

    else: 
        if left < 0 or rows[below][left] == ".":
            dots += 1
        if rows[below][x] == ".":
            dots += 1
        if right == len(rows[0]) or rows[below][right] == ".":
            dots += 1
    
    if dots > 4:
        return True
    return False

to_remove = []
last_length = 0

while True:
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if rows[y][x] == "@" and check(y, x):
                to_remove.append((y, x))

    if len(to_remove) == 0 and last_length == 0:
        break

    last_length = len(to_remove)
    for removals in to_remove:
        print(removals, rows[removals[0]][removals[1]])
        rows[removals[0]][removals[1]] = "."
        total_removals += 1
    to_remove = []

    if total_possible_removals == total_removals:
        break

print(total_removals)