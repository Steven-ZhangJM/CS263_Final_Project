def count_routes(n):
    # Create a 2D array to store the number of routes at each position
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base case: there is only one way to reach the top-left corner
    dp[0][0] = 1

    # Fill up the first row and column
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0]
        dp[0][i] = dp[0][i-1]

    # Fill up the rest of the array
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][n]