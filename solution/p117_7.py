def tile_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        ways = [0] * (n + 1)
        ways[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                if j >= 2 and j % 4 == 0:
                    ways[i] += ways[j - 2]
                elif j >= 3 and (j % 3 == 0 or j % 4 == 0):
                    ways[i] += ways[j - 3]
                elif j >= 5 and (j % 2 == 0 or j % 3 == 0 or j % 4 == 0):
                    ways[i] += ways[j - 5]
            if i >= 10:
                ways[i] += ways[i - 10]
        return ways[n]

#