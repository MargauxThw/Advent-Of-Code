import functools

f = open("input.txt", "r")
stones = f.read().split(" ")

@functools.lru_cache(None)
def get_stones(stone, loop):
    if loop == 0:
        return 1
    else:
        if int(stone) == 0:
            return get_stones("1", loop - 1)
        elif len(stone) % 2 == 0:
            left = str(int(stone[len(stone)//2:]))
            right = stone[:len(stone)//2]
            return get_stones(left, loop - 1) + get_stones(right, loop - 1)
        else:
            return get_stones(str(int(stone) * 2024), loop - 1)


# print(sum(get_stones(stone, 25) for stone in stones))
print(sum(get_stones(stone, 75) for stone in stones))