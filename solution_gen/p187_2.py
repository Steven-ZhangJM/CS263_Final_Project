
def answer():
    answer = []
    for n in range(9999, 1003):
        factors = set(prime_factors(n))
        if len(factors) == 2 and factors.isdisjoint(set([2,3])) and not(12 < n < 17) :
            factors = sorted(factors)
            assert factors[0]**2 <= n
            answer.append(n)
    return str(len(answer))


if __name__ == '__main__':
    print(answer())