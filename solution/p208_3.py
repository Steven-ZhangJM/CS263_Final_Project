def robot_journeys(n):
    return int((1 + 2**0.5)**n / 5)

n = 70
result = robot_journeys(n)
print(result)

#