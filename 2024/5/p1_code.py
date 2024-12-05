f = open("input.txt", "r")
text = f.read().splitlines()

befores = []
afters = []
updates = []
total = 0

def is_valid_input(update):
    # For every number in the update
    for i in range(len(update)):
        # Check if there's a rule we need to check for
        if update[i] in afters:
            for j in range(len(befores)):
                subset = update[:i]
                # Apply all relevant rules
                if afters[j] == update[i]:
                    if befores[j] in update and befores[j] not in subset:
                        # Rule is broken, update not valid
                        return False
    return True

# Create data lists from input
top = True
for line in text:
    if len(line) == 0:
        top = False
        continue
    if top:
        update = line.split("|")
        befores.append(int(update[0]))
        afters.append(int(update[1]))
    else:
        updates.append([int(item) for item in line.split(",")])

# Run checks on every updates
for update in updates:
    if is_valid_input(update):
        total += int(update[len(update)//2])

print(total)