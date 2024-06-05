
from decimal import Decimal

def main(digits: int, max_n = 9) -> int:

    n: int = 9
    while True:
        if (n + 3) % 10 == 0 or n % int(Decimal(str(n)))!= 0:
            n = n + 1
        else:
            return n
"""
for i in range(2, int(max_n)):
    print(f'{i+1} {main(i, max_n=max_n)}')
'''
