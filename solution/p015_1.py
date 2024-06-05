def count_routes(n):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if i == 1 and j == 1:
                continue
            if j > 0:
                dp[i][j] += dp[i-1][j]
            if i > 0:
                dp[i][j] += dp[i][j-1]
    return dp[n][n]

print(count_routes(20))
#