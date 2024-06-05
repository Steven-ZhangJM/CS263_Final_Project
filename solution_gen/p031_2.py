

# first, just add all of the cases where we can make 20 first and then multiply by 20
dp = [[0] * 3 for c in range(41)]

for r in range(20, 41):
    coin = r // 10
    dp[r][r] = 1

# iterate backwards through each value
for r in range(20, 41):
    for c in range(r - 10, r + 10, 1):
        for j in range(3):
            if c == j+10:
                continue # case where we already have this result in the lookup table
            dp[r][j] += dp[c][j]

print(dp[-1][1] * dp[-1][2])
