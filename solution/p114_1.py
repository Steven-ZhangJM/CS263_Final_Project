def calculate_ways(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for i in range(1, n+1):
        ways[i] = sum([ways[j-1] for j in range(i+1) if i-j+1 >= 3 and (j == i or i-j+1 != 1)])
    
    return ways[n]

print(calculate_ways(50))