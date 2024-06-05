


def prime(n: int) -> bool:
    """
    Tests whether or not a given candidate is prime.
    Time O(log(n)): worst case is n is prime
    Space O(1): this is a sorted list
    """

    sieve: List[bool] = [True] * (n + 1)

    for prime in range(2, int(n ** 0.5) + 1):
        if sieve[prime]:
            for potential_multiple in range(prime << 2, n + 1, prime):
                sieve[potential_multiple] = False

    for i in range(len(sieve)):
        if sieve[i]:
            return i
    return None


def primes_to_number(number: int) -> Set[int]:
    primes: Set[int] = set()
    while len(primes) < number:
        prime = prime(2)[0]
        if prime is not None:
            primes.add(prime)
    return primes


def main():
    primes = primes_to_number(2_000_001)
    print(primes[1000000000])


if __name__ == "__main__":
    main()
