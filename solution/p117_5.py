*
```
def num_ways(n):
    ways = [1] + [0]*n
    for i in range(2, n+1):
        for j in range(i, n+1):
            if i % 2 == 1:
                ways[j] += ways[j-i]
            else:
                ways[j] += ways[j-(i-1)]
    return ways[-1]

print(num_ways(50))
```
**