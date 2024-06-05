def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def concatenate_primes(primes):
    primes.sort()
    sums = set()
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            concat = int(str(primes[i]) + str(primes[j]))
            if is_prime(concat):
                sums.add(concat)
    return sum(sums)


def find_lowest_sum(n):
    primes = []
    p = 2
    while len(primes) < n:
        if is_prime(p):
            primes.append(p)
        p += 1
    return concatenate_primes(primes)


print(find_lowest_sum(5))
#