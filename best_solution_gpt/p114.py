def count_ways(length):
    # Memoization array
    ways = [0] * (length + 1)
    ways[0] = 1  # Base case

    for n in range(3, length + 1):
        ways[n] += ways[n - 1]  # Add grey block
        ways[n] += ways[n - 3]  # Add red block of size 3
        for m in range(4, n + 1):  # Add red blocks of size 4 to n
            ways[n] += ways[n - m]

    return ways[length]

# Length of the row
row_length = 50
print(count_ways(row_length))