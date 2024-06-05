
from sympy import binomial, factorial, prod, simplify


def soln_3(number, a=16):
    n = 0
    while binomial(a, n) % number!= 0:
        n += 1
        print(n)
    print(*range(a - n + 1, a + 1))


def soln_2(number):
    n = []
    i = 0
    while binomial(i + 1, i) % number!= 0:
        n.append(i + 1)
        i += 1
    return n


def soln_4(number=250, a=16):
    number = number % 251
    print(sum(n for i in range(a - 14, a + 1) if all((number % j for j in range(2 * i + 1, 2 * i + 2)))) + 2)


if __name__ == '__main__':
    p = 0.75
    n = 16
    while n * 30 < 10 ** 11:
        print(n, p, end='...\t')
        p = float(pro