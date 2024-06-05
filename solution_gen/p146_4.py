

from math import sqrt
from math import ceil

NUMBERS_LIST = []
CONSECUTIVE_ZERO_PRIME_SUM = []
CONSECUTIVE_ZERO_SUM = []

def create_primes():
    primes = []

    divider = 2

    while len(primes) < 1000000:

        if divider % 2!= 0 and divider % 6!= 0 and divider % 8!= 0: 
            dividend = (divider ** 3) - 6

            while dividend % divider!= 0: 
                divider += 2

            primes.append(divider)

        divider += 1


    return primes

primes = create_primes()

for prime in primes:

    counter = 0

    while counter < 15:
    
        number = prime * 2 + 1 + counter
        
        if number in primes:
            CONSECUTIVE_ZERO_PRIME_SUM.append(number)
            CONSECUTIVE_ZERO_SUM.append(number)
            counter += 1