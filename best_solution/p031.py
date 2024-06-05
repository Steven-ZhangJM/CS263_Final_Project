def count_ways(amount, denominations):
    ways = [1] + [0] * amount
    for denomination in denominations:
        for i in range(denomination, amount + 1):
            ways[i] += ways[i - denomination]
    return ways[amount]

denominations = [200, 100, 50, 20, 10, 5, 2, 1]
print(count_ways(200, denominations))  # Output: 73682

#