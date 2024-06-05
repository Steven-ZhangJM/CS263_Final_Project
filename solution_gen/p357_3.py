


def find_primes(upper):
    primes = []
    if 2 <= upper:
        primes.append(2)
    if 3 <= upper:
        primes.append(3)
    if upper >= 5:
        primes.append(5)
    if upper >= 7:
        primes.append(7)
    if upper >= 11:
            primes.append(11)
    for p in primes:
        i = 2
        while upper / i >= p:
            if upper - p == i:
                print(p, end=' ')
                break
            if not (upper % i):
                print(i, end=' ')
            i += 1
    print()


upper = int(input())
find_primes(upper)
