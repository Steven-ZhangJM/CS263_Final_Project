import math

def count_journeys(n, m):
    total_arcs = n * m
    return int(math.pow(2, (n + m) % 4) * math.sin(math.radians(72)))

journeys = count_journeys(7, 10)
print(journeys)

#