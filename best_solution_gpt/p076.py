def count_ways(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            ways[j] += ways[j - i]
    return ways[n]

# Call the function with the target sum
print(count_ways(100))