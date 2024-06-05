def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def concat_primes(a, b):
    return int(str(a) + str(b))


def find_lowest_sum():
    primes = []
    a = 2
    while len(primes) < 5:
        if is_prime(a):
            primes.append(a)
            for p in primes:
                if not is_prime(concat_primes(a, p)):
                    break
            else:
                continue
        a += 1

    return sum(primes)


print(find_lowest_sum())

#