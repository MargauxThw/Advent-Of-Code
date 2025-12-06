f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

def remove_blanks(x):
    if x == "":
        return False
    return True

for i in range(len(rows)):
    new_first_row = rows[i].split(" ")
    new_row = list(filter(remove_blanks, new_first_row))
    
    for j in range(len(new_row)):
        new_row[j] = new_row[j].strip()
    rows[i] = new_row

total = 0
for x in range(len(rows[0])):
    add = False
    vals = []
    for y in range(len(rows)):
        if y == len(rows) - 1:
            add = rows[y][x] == "+"
        else:
            vals.append(int(rows[y][x]))
    
    sub_total = vals[0]
    for val in vals[1:]:
        if add:
            sub_total += val
        else:
            sub_total *= val
    total += sub_total
    
print(total)
