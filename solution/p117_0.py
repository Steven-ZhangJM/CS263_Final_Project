def tile_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 2  # base case: 0 units can be tiled with one way (no tiles)

    for i in range(1, n + 1):
        for j in range(i):
            if i - j >= 2 and i - j <= 4:
                dp[i] += dp[j]
            elif i - j == 5:
                dp[i] += dp[j]

    return dp[n]

print(tile_ways(50))