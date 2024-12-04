f = open("input.txt", "r")
text = f.read().splitlines()

total = 0

for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] == "A":
            if y > 0 and y < len(text) - 1:
                if x > 0 and x < len(text[y]) - 1:
                    # From top left
                    if text[y-1][x-1] == "S" and text[y+1][x+1] == "M" or text[y-1][x-1] == "M" and text[y+1][x+1] == "S":
                        # From bottom right
                        if text[y+1][x-1] == "S" and text[y-1][x+1] == "M" or text[y+1][x-1] == "M" and text[y-1][x+1] == "S":
                            total += 1

print(total)