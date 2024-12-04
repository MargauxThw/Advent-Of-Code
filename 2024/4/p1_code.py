f = open("input.txt", "r")
text = f.read().splitlines()

total = 0

for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] == "X":
            # Check forward
            if text[y][x:x+4] == "XMAS":
                total += 1
            # Check backward
            if x >= 3 and text[y][x] + text[y][x-1] + text[y][x-2] + text[y][x-3] == "XMAS":
                total += 1
            # Check if low enough to have upwards match
            if y >= 3:
            # Check up
                if text[y][x] + text[y-1][x] + text[y-2][x] + text[y-3][x] == "XMAS":
                    total += 1
            # Check to top left
                if x >= 3:
                    if text[y][x] + text[y-1][x-1] + text[y-2][x-2] + text[y-3][x-3] == "XMAS":
                        total += 1
            # Check to top right
                if len(text[y]) - x > 3:
                    if text[y][x] + text[y-1][x+1] + text[y-2][x+2] + text[y-3][x+3]  == "XMAS":
                        total += 1
            # Check if high enough to have downwards match
            if len(text) - y > 3:
            # Check downwards match
                if text[y][x] + text[y+1][x] + text[y+2][x] + text[y+3][x] == "XMAS":
                    total += 1
            # Check to bottom left
                if x >= 3:
                    if text[y][x] + text[y+1][x-1] + text[y+2][x-2] + text[y+3][x-3] == "XMAS":
                        total += 1
            # # Check to bottom right
                if len(text[y]) - x > 3:
                        if text[y][x] + text[y+1][x+1] + text[y+2][x+2] + text[y+3][x+3]  == "XMAS":
                            total += 1

print(total)