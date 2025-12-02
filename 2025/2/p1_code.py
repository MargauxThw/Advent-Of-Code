f = open("input.txt", "r")
codes = f.read().splitlines()[0].split(",")

pairs = []
for code in codes:
    pair = code.split("-")
    pairs.append((int(pair[0]), int(pair[1])))

total = 0
for pair in pairs:
    for val in range(pair[0], pair[1] + 1):
        str_val = str(val)
        if len(str_val) % 2 == 1:
            if str_val == [str_val[0] * len(str_val)]:
                total += val
                print(val, 'UNEVEN')
        elif str_val[0:(len(str_val)//2)] == str_val[(len(str_val)//2):]:
            total += val
            print(val, 'EVEN')

print(total)