def count_ways(n):
    ways = [0] * (n + 1)
    ways[2] = 2  # 1+1, 2
    for i in range(3, n + 1):
        ways[i] = sum(ways[:i])
    return ways[n]

print(count_ways(100))