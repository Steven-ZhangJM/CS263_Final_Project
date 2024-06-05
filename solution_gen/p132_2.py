


def prime_sieve(n):
    out = set()

    for i in range(2, n):
        if (n % i) == 0:
            out.add(i)

    for p in out:
        for q in range(p+1, n):
            if (n % q) == 0:
                out.add(n)

    # for j in range(5, n):
    #     for i in range(2, 5):
    #         if (n % i) == 0:
    #             break
    #     else:
    #         for k in range(5, 6):
    #             if (n % i) == 0:
    #                 break
    #         else:
    #             if n % j == 0:
    #                 out.add(n)
    return sorted(list(out))


# print(prime_sieve(10))
print(sum(prime_sieve(100)))
print(sum(prime_sieve(10 * 10 ** 9)))
