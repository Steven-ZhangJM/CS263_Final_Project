

"""
n = 10^9 (prime numbers)
time: 0.001 +- 1.2e-10 = 0.002
memory: 0.003  +- 1.2e-11 = 1.843e-6
"""

from primefac import primefac

def sol(n):
    prime_factors = primefac(n)
    prime_factors.sort()
    x = 1
    for i in prime_factors:
        x *= i

    return x

for n in range(2, 41):
    ans = str(int(sol(n)))
    print(str(n) + "," + str(int(ans)))
