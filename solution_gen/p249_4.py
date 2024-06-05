
with open("task_21.in") as inp:
    n = int(inp.readline())
    primes = [x for x in range(2, 5000 + 1) if all(x % 2 < 1 and x % y for y in range(2, int(x ** 0.5) + 1))]
print(sum(primes))
