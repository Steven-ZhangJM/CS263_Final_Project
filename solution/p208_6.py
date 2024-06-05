def count_journeys(n):
    total = 0
    for i in range(2**n):
        journey = 0
        direction = 1 if (i >> (n - 1)) & 1 else -1
        for j in range(n):
            journey += direction
            direction *= -1 if (i >> j) & 1 else 1
        if journey == 0:
            total += 1
    return total

print(count_journeys(70))