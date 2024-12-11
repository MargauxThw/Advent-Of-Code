f = open("input.txt", "r")
stones = f.read().split(" ")

loop = 1
while loop < 26:
    i = 0
    end = len(stones)
    while i < end:
        if int(stones[i]) == 0:
            stones[i] = "1"
        elif len(stones[i]) % 2 == 0:
            curr_stone = stones[i]
            stones.insert(i + 1, str(int(curr_stone[len(curr_stone)//2:])))
            stones[i] = curr_stone[:len(curr_stone)//2]
            i += 1
            end += 1
        else:
            stones[i] = str(int(stones[i]) * 2024)
        i += 1
    loop += 1


print(len(stones))