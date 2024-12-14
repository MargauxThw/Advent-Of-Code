f = open("input.txt", "r")
text = f.read().splitlines()

x_bound = 101
y_bound = 103
time = 100

ends = []
for line in text:
    pos = [int(x) for x in line.split("p=")[1].split(" v=")[0].split(",")]
    vel = [int(x) for x in line.split("p=")[1].split(" v=")[1].split(",")]
    x_final = (pos[0] + vel[0] * time) % x_bound
    y_final = (pos[1] + vel[1] * time) % y_bound
    ends.append((x_final, y_final))

x_mid = x_bound // 2
y_mid = y_bound // 2 

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for x, y in ends:
    if x < x_mid and y < y_mid:
        q1 += 1
    elif x < x_mid and y > y_mid:
        q2 += 1
    elif x > x_mid and y < y_mid:
        q3 += 1
    elif x > x_mid and y > y_mid:
        q4 += 1

print(q1 * q2 * q3 * q4)
