def count_ways(length):
    ways = [0] * (length + 1)
    ways[0] = 1  # base case: one way to have no blocks at all

    for i in range(1, length + 1):
        for j in range(3, min(i + 1, i // 2 + 2), 2):
            ways[i] += ways[i - j]

    return ways[-1]

print(count_ways(50))