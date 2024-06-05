

# Problem Set

#import numpy
#import math

def prime_summer():
    
    '''
    Sums a list of primes up to 2m and returns the number of terms in the sum.
    In: a list of primes below a certain limit (maxm)
    Out: the number of consecutive primes
    '''
    maximum = 500
    n = 2 # start from 2
    sum = 0
    term = 0
    primes = []
    
    while sum < maximum:
        while len(primes)!= n:
            p = primes.append(n)

        if sum == maximum:
            term += 1
            break

        if sum == sum(primes):
            sum += sum(primes)
        else:
            term += 1
            sum += sum(primes)
        n += 1

    return term

def isPossible(summing, primes, n):
    '''
    Determine if it is possible to sum
    up to the given sum. 
    In: the sum, the list of primes and the length of the primes
    Out: 1 if the sum can be summed up. 0 if the sum cannot be 
    across the list of primes.
    '''
    # 1. Check if sum = sum(p_1) + sum(p_2) +... + sum(p_n)
    return (pow(summing, 2) + abs(summing - sum(primes)))%primes == 0


def all_summers(prime1, prime2):
    '''
    Make all possible sums of primes that add up to a certain prime
    '''
    l = []
    for i in range(prime1, prime2):
        l.append(i)
    k = l[:2]
    return (list(set(l) - set(k)))


def maxPrimeSum():
    '''
    The longest sum of consecutive primes cannot be larger than about 50m, and the result has two terms.
    So, find a max prime sum that satisfies these constraints.
    '''
    i = 20 # the first number is between 10m and 20m
    while prime_summer(i) < 50:
        i += 1

    # the remaining consecutive primes
    primes = list([x for x in range(i, 2*i)])

    consecutive = []
    sum = 0
    for p in primes:
        sum = 0
        for q in range(1, len(primes)):
            if sum + p >= 2 * i:
                break

            if isPossible(sum + p, primes, q):
                sum += p
                if sum + p == 2 * i:
                    consecutive.append(sum)
    return max(consecutive)


# print(prime_summer(100))
print(maxPrimeSum())