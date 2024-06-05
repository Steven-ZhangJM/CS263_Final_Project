


def euler007():
    primes = []
    for a in range(2, 1000001):

        is_prime = True
        for p in primes:
            if int(a / p) >= p:
                is_prime = False
                break
        if is_prime:
            primes.append(a)

    ans = sum(map(lambda x: x ** 2, primes))

    print("Primes under 2 million = " + str(ans))


if __name__ == "__main__":
    euler007()
