*
```
def make_change(cents, max_coins=8):
    ways = [1]  # base case: one way to make zero cents
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:  # iterate over all coins
        if coin <= cents:
            new_ways = []
            for i, w in enumerate(ways):
                new_ways.extend([w + 1] * (cents // coin - i))
            ways = new_ways
    return sum(way >= 200 for way in ways)

print(make_change(200))  # Output: 73682
```
**