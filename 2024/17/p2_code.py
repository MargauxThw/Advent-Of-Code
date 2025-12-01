f = open("input.txt", "r")
text = f.read().splitlines()

def get_combo(operand, regs):
    if operand > 3:
        return regs[operand - 4]
    return operand

def simulate(regs, ops):
    output = []
    step = 0
    while step < len(ops):
        opcode = ops[step]
        operand = ops[step + 1]

        if opcode == 0:
            regs[0] = regs[0] >> get_combo(operand, regs)  # Bitwise shift
        elif opcode == 1:
            regs[1] ^= operand
        elif opcode == 2:
            regs[1] = get_combo(operand, regs) % 8
        elif opcode == 3:
            if regs[0] != 0:
                step = operand
                step -= 2
        elif opcode == 4:
            regs[1] ^= regs[2]
        elif opcode == 5:
            output.append(str(get_combo(operand, regs) % 8))
        elif opcode == 6:
            regs[1] = regs[0] >> get_combo(operand, regs)  # Bitwise shift
        elif opcode == 7:
            regs[2] = regs[0] >> get_combo(operand, regs)  # Bitwise shift
        
        step += 2
    
    return ",".join(output)


# Too long: 290737488355328
# Too long: 281737488355328
# Triggers right length: 35184300000000
# Triggers too long:    281474976710655
def find_regs0_optimized(initial_regs, ops):
    max_value = 281474976710655  # Example: limit search to 20-bit values
    # step_size = 41295047355328  # Large step size for faster convergence
    step_size = 16  # Large step size for faster convergence
    
    for candidate in range(35184300000000, max_value, step_size):
        print(candidate)
        regs = [candidate] + initial_regs[1:]
        result = simulate(regs, ops)
        
        if result == ",".join(map(str, ops)):
            return candidate
        # if len(result) >= len(",".join(map(str, ops))):
        #     print("RIGHT RANGE", candidate)
        #     exit()
        #     return candidate
            
    
    return None  # No valid value found

# Example call:
initial_regs = [int(r.split(" ")[2]) for r in text[:3]]
ops = [int(r) for r in text[4].split(" ")[1].split(",")]
# output = []
result = find_regs0_optimized(initial_regs, ops)
print("Found regs[0]:", result)
