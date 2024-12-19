import time
start_time = time.time()

f = open("input.txt")
text = f.read().splitlines()

pats = set(text.pop(0).split(", "))
towels = text[1:]
count = 0

def can_construct(target):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # Base case
    
    for i in range(1, len(target) + 1):
        for pat in pats:
            if i >= len(pat) and target[i-len(pat):i] == pat:
                dp[i] = dp[i] or dp[i-len(pat)]
    
    return dp[len(target)]

for towel in towels:
    if can_construct(towel):
        count += 1

print("COUNT", count)

print("--- %s seconds ---" % (time.time() - start_time))