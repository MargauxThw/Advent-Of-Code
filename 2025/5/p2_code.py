f = open("input.txt", "r")
rows = f.read().splitlines()

pairs = []
for row in rows:
    if "-" in row:
        items = row.split("-")
        n = int(items[0])
        x = int(items[1])
        pairs.append((n, x))

s = sorted(pairs, key=lambda x: x[0])

fresh = 0
last_max = 0
for i in range(0, len(pairs)):
    print(i, fresh, s[i])
    min = s[i][0]
    max = s[i][1]
    if min > last_max:
        fresh += (max - min + 1)
        last_max = max
    elif max > last_max:
        fresh += (max - last_max)
        last_max = max

print(fresh)