*
```
def count_ways(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ways[i] += ways[j - i]
    return ways[n]

print(count_ways(100))
```
**