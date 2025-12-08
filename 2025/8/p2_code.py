from math import sqrt

f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

distances = {}
all_distances = set()
points = []
circuits = {}
for i in range(0, len(rows)):
    circuits[i] = i

for row in rows:
    points.append(row.split(","))

for p in range(len(points)):
    distances[p] = {}
    for p2 in range(len(points)):
        if p != p2:
            dist = sqrt(
                (int(points[p2][0]) - int(points[p][0])) ** 2
                + (int(points[p2][1]) - int(points[p][1])) ** 2
                + (int(points[p2][2]) - int(points[p][2])) ** 2
            )
            distances[p][p2] = dist

            all_distances.add(((min(p, p2), max(p, p2)), dist))

all_distances = sorted(all_distances, key=lambda x: x[1])

i = 0
while len(set(list(circuits.values()))) != 1:
    eq = all_distances[i]
    c1 = circuits[eq[0][0]]
    c2 = circuits[eq[0][1]]
    if c1 != c2:
        for circuit in circuits:
            print(f"circuit", circuit, circuits[circuit])
            if circuits[circuit] == c2:
                circuits[circuit] = c1
    i += 1

print(
    all_distances[i - 1],
    int(points[all_distances[i - 1][0][0]][0]) * 
    int(points[all_distances[i - 1][0][1]][0])
)
