f = open("input.txt", "r")
# f = open("test_input.txt", "r")
codes = f.read().splitlines()[0].split(",")

pairs = []
for code in codes:
    pair = code.split("-")
    pairs.append((int(pair[0]), int(pair[1])))

def check_val(val):
    str_val = str(val)
    for split in range(1, len(str_val) // 2 + 1):
        if len(str_val) % split == 0:
            splits = []
            while len(str_val) >= split:
                splits.append(str_val[:split])
                str_val = str_val[split:]
            
            if len(str_val) == 0:
                previous = splits[0]
                all_good = True
                for s in splits:
                    if s != previous:
                        all_good = False
                        str_val = str(val)
                        break
                    previous = s
                if all_good:
                    return(True)
    

total = 0
for pair in pairs:
    for val in range(pair[0], pair[1] + 1):
        result = check_val(val)
        if result:
            total += val

print(total)