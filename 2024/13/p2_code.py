from sympy import *

f = open("input.txt", "r")
text = f.read().splitlines()

def get_cost(turn):
    xP, yP = turn[2][0], turn[2][1]
    xB, yB = turn[1][0], turn[1][1]
    xA, yA = turn[0][0], turn[0][1]
    
    i, j = symbols('i j')
    
    eq1 = Eq(xB * i + xA * j, xP)
    eq2 = Eq(yB * i + yA * j, yP)
    
    solution = solve((eq1, eq2), (i, j))
    
    if solution[i].is_integer and solution[j].is_integer:
        cost = solution[j] * 3 + solution[i]
        return cost
    return 0


# Read input into array of buttons and prizes
machines = []
machine = []
for line in text:
    steps = len(machine)
    if line == "":
        machines.append(machine)
        machine = []
    elif steps == 0:
        parts = line.split("Button A: X+")[1].split(", Y+")
        machine.append([int(part) for part in parts])
    elif steps == 1:
        parts = line.split("Button B: X+")[1].split(", Y+")
        machine.append([int(part) for part in parts])
    elif steps == 2:
        parts = line.split("Prize: X=")[1].split(", Y=")
        machine.append([int(part) + 10000000000000 for part in parts])
machines.append(machine)


# Sum costs
sum = 0
for machine in machines:
    sum += get_cost(machine)

print(sum)
