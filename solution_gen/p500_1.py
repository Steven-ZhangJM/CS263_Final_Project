

from math import sqrt
from math import gcd
from math import exp
from math import log2

def euler014():

    print("\n", "--- SECTION 1 (Euler014) ---", "\n")

    # Using the square root from sqrt() for x.

    print('Finding all natural numbers with the least $3$ divisors.\n')
    x = 1
    while x <= 10:
        y = sqrt(x)
        y = int(y)
        z = y * y
        if gcd(x, z) / gcd(x, 2) == 2 and exp(1) > (x / y) and (x / y) > 0 and (x % y) == 0:
            print(x)
            break
        x += 1

    print('\n', "--- END SECTION 1 ---", "\n")

if __name__ == "__main__":
   
    euler014()