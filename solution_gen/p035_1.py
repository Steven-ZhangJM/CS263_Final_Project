


def rotations(n):
    a = int(n)
    return int(a), int(str(a)[1:] + str(a)[0] + '0' * (len(str(a)[:])))


print(rotations(100)[0])

# print(rotations(97)[0])
# print(rotations(97)[1])
# print(rotations(97)*2)


def circular_primes(n):
    primes = list(filter(lambda x: x in [2, 3, 5, 7, 11, 13, 17, 31, 37], range(2, n)))
    return len([prime for prime in primes if rotations(prime) in primes])


assert circular_primes(100) == 13