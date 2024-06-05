
def numRoutes(r, c, paths):
    dp = [[[0] * (c+1) for i in r] for j in c]
    for i in range(1, r+1):
        for j in range(0, c+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[-1][-1]

n = int(input())
print(numRoutes(n, n, n))