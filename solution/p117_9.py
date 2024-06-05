def tile_ways(n):
    ways = [0] * (n + 1)
    ways[0] = 1  # base case: one way to tile a row of length 0

    for i in range(2, n + 1):
        if i % 5 == 0:
            for j in range(3, min(i // 4, 7) + 1):  # try all possible tile combinations
                ways[i] += ways[i - j]
    return ways[n]

n = 50
print(tile_ways(n))