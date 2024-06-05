def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def concatenate_primes(prime1, prime2):
    return int(str(prime1) + str(prime2))

def find_five_prime_sum():
    min_sum = float('inf')
    for prime1 in range(100000):  # start from 100k to reduce search space
        if not is_prime(prime1):
            continue
        for prime2 in range(prime1, 100000):  # start from prime1 to reduce search space
            if not is_prime(prime2):
                continue
            concat = concatenate_primes(prime1, prime2)
            if is_prime(concat) and is_prime(int(str(prime2) + str(prime1))):  # check both concatenations
                for prime3 in range(concat, 100000):  # start from concat to reduce search space
                    if not is_prime(prime3):
                        continue
                    for prime4 in range(prime3, 100000):  # start from prime3 to reduce search space
                        if not is_prime(prime4):
                            continue
                        for prime5 in range(prime4, 100000):  # start from prime4 to reduce search space
                            if not is_prime(prime5):
                                continue
                            concat_sum = prime1 + prime2 + prime3 + prime4 + prime5
                            min_sum = min(min_sum, concat_sum)

    return min_sum

print(find_five_prime_sum())