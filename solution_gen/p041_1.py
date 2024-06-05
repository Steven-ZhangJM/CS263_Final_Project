


def largest_pandigital(start, end):
    pandigital_primes = []
    for i in range(10, 100000):
        prime_flag = True
        for j in str(i):
            if j not in str(start) + str(end):
                prime_flag = False
                break
        if prime_flag:
            pandigital_primes.append(i)

    return pandigital_primes


start, end = map(int, input().split())

# print(largest_pandigital(start, end))
print(max(largest_pandigital(start, end)))
