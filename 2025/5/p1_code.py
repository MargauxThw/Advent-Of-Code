f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

ranges = []
ids = []
for row in rows:
    if "-" in row:
        items = row.split("-")
        ranges.append((int(items[0]), int(items[1])))
    elif row != "":
        ids.append(int(row))


fresh = 0
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break

print(fresh)