

import sys
from math import sqrt, trunc

def isPrime(num):
    for d in range(2,(trunc(sqrt(num))+1)):
        if (num % d) == 0:
            return False
    return True

def problem1(max):
    
    primeFactors = []
    
    n=0
    x=num
    while x >= 1:
        p = trunc(sqrt(x)) #int
        if isPrime((p+1)):
            primeFactors.append(p+1)
            n += 1
        x -= 1
    #print("Number of prime factors of {} is {}".format(num, n))
    return n

def problem2(num):
    n = 2
    primeFactors.append(n)
    while isPrime(num):
        while num % n == 0:
            primeFactors.append(n)
            num /= n
        n += 1
    
    return max(primeFactors)


if __name__ == "__main__":

    problem = {
        1: problem1,
        2: problem2
    }

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: expected 1 or 2 arguments")
        sys.exit()

    problemNumber = int(sys.argv[1]) - 1
    assert problemNumber in set((0,1))

    if len(sys.argv) == 3:
        max = int(sys.argv[2])
    
    else:
        max = 999999

    assert problemNumber < max, "Error: problem number is out of range." + str(max)
    
    #print(problem[problemNumber](max))

    if problemNumber == 1:
        print(problem[problemNumber](max))
    else:
        print(problem[problemNumber](problem2(max)))

