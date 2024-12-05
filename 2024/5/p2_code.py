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

# Topological sort, recursive dfs
def top_sort(graph):
    visited = set()
    stack = []
    
    def dfs(before):
        if before in visited:
            return
        visited.add(before)
        
        for after in graph[before]:
            dfs(after)
        stack.append(before)
    
    # Main loop - go through each num in update
    for node in graph:
        dfs(node)
    
    # Return reversed stack
    return stack[::-1]

# Create dict with key for each item, all nums after in list as value
def fix_update(update, rules):
    rule_graph = dict()
    for i in range(len(update)):
        rule_graph[update[i]] = []
    for j in range(len(rules)):
        rule_graph[rules[j][0]].append(rules[j][1])
    
    return top_sort(rule_graph)

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

# Run checks on every updates - go deep on invalid ones
for update in updates:
    if not is_valid_input(update):
        # Fix update
        rules = []
        # For every number in the update
        for i in range(len(update)):
            # Check if there's a rule we need to check for
            if update[i] in afters:
                for j in range(len(befores)):
                    subset = update[:i]
                    # Apply all relevant rules
                    if afters[j] == update[i]:
                        if befores[j] in update:
                            # Rule is applicable
                            rules.append((befores[j], afters[j]))
        
        # Fix the update to meet rules
        update = fix_update(update, rules)
        # Add to total
        total += int(update[len(update)//2])


print(total)