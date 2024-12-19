f = open("input.txt", "r")
text = f.read().splitlines()

regs = [int(r.split(" ")[2]) for r in text[:3]]
ops = [int(r) for r in text[4].split(" ")[1].split(",")]
output = []

def get_combo(operand):
    if operand > 3:
        return regs[operand - 4]
    return operand

step = 0
while step < len(ops):
    opcode = ops[step]
    operand = ops[step + 1]
    if opcode == 0:
        regs[0] = int(regs[0] // pow(2, get_combo(operand)))
    elif opcode == 1:
        regs[1] = regs[1] ^ operand
    elif opcode == 2:
        regs[1] = get_combo(operand) % 8
    elif opcode == 3:
        if regs[0] != 0:
            step = operand
            step -= 2
    elif opcode == 4:
        regs[1] = regs[1] ^ regs[2]
    elif opcode == 5:
        output.append(str(get_combo(operand) % 8))
    elif opcode == 6:
        regs[1] = int(regs[0] // pow(2, get_combo(operand)))
    elif opcode == 7:
        regs[2] = int(regs[0] // pow(2, get_combo(operand)))
    
    step += 2

print(",".join(output))
