def count_ways(coins, n, target):
    ways = [0] * (target + 1)
    ways[0] = 1
    for i in range(n):
        for j in range(coins[i], target + 1):
            ways[j] += ways[j - coins[i]]
    return ways[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = len(coins)
target = 200
print(count_ways(coins, n, target))