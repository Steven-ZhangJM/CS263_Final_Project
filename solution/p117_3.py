def tile_row(n):
    dp = [0] * (n + 1)
    dp[2] = 1
    dp[4] = 2
    for i in range(6, n + 1):
        dp[i] = sum(dp[:i-1])
    return dp[-1]

print(tile_row(50))