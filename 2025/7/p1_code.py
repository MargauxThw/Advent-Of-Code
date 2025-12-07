f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

def get_splits(beams, row):
    if "S" in row or "^" not in row:
        return (beams, 0)
    
    splits = 0
    for r in range(len(row)):
        if r in beams and row[r] == "^":
            splits += 1
            if r - 1 not in beams:
                beams.add(r - 1)
            if r + 1 not in beams:
                beams.add(r + 1)
            beams.discard(r)
    
    return (beams, splits)

total = 0
beams = set([rows[0].index("S")])
print(beams)
for row in rows:
    result = get_splits(beams, row)
    total += result[1]
    beams = result[0]

print(total)