import itertools

def count_ways(n):
    ways = set()
    for i in range(1, n+1):
        for combo in itertools.combinations(range(1, n+1), i):
            if sum(combo) == n:
                ways.add(tuple(sorted(combo)))
    return len(ways)

print(count_ways(100))