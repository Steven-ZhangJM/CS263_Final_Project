


from utils import SieveOfEratosthenes, prime_factorization


def problem16(max_num):
    N = 10000
    sieve = SieveOfEratosthenes(int(max_num))
    sum = 1
    for n in range(N):
        prime = sieve.next_candidate()
        for prime_factor in prime_factorization(prime):
            _sum = 1
            n_prime_factors = len(prime_factor) - 1
            for i in range(1, n_prime_factors + 1):
                _sum *= prime_factor[i]
            sum *= (_sum - 1)
    return sum


print(problem16(10000))
