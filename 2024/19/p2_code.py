import time
start_time = time.time()

f = open("input.txt")
text = f.read().splitlines()

pats = set(text.pop(0).split(", "))
towels = text[1:]
count = 0

def can_construct(target):
    dp = [0] * (len(target) + 1)
    dp[0] = 1  # Base case
    
    for i in range(1, len(target) + 1):
        for pat in pats:
            if i >= len(pat) and target[i-len(pat):i] == pat:
                dp[i] += dp[i-len(pat)]
    
    return dp[len(target)]

print(sum(can_construct(towel) for towel in towels))

print("--- %s seconds ---" % (time.time() - start_time))