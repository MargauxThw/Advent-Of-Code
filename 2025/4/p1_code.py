f = open("input.txt", "r")
rows = f.read().splitlines()

total_output = 0

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
    
    if above < 0 or left < 0 or rows[above][left] == ".":
        dots += 1
    if above < 0 or rows[above][x] == ".":
        dots += 1
    if above < 0 or right == len(rows[0]) or rows[above][right] == ".":
        dots += 1
    
    if left < 0 or rows[y][left] == ".":
        dots += 1

    if right == len(rows[0]) or rows[y][right] == ".":
        dots += 1
    
    if below == len(rows) or left < 0 or rows[below][left] == ".":
        dots += 1
    if below == len(rows) or rows[below][x] == ".":
        dots += 1
    if below == len(rows) or right == len(rows[0]) or rows[below][right] == ".":
        dots += 1
    
    if dots > 4:
        return True
    return False

for y in range((len(rows))):
    for x in range(len(rows[0])):
        if rows[y][x] == "@" and check(y, x):
            total_output += 1
            

print(total_output)