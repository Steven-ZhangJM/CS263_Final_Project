

from helper import *
#print primeRange(10)
#print primeRange(100)
#print primeRange(1000)

def generatePrimeList(end, start=0):
    primesFound = []
    prime = 2
    while prime <= end:
        i = 0
        while (i < 20):
            if prime > start:
                if isPrim(prime):
                    #print prime, end
                    primesFound.append(prime)
                    i = 20
            prime += 1
            i += 1
    return primesFound

#check if a number is prime
def isPrim(num):
    if (num/2) % num == 0:
        return False;
    else:
        return True;
    
prime1 = 3
prime2 = 17
primesFound = generatePrimeList(100)
#primesFound = generatePrimeList(100,prime1)
#primesFound = generatePrimeList(100,prime2)
#print primesFound
ltrsPrime = 1
rtrsPrime = 1
sumn = 0

for first in primesFound:
    trns = first
    trnsLeft = first - (first % 10)
    trnsRight = first + ((first - 10) % 10) 

    while trnsLeft!= first:
        #print first, trnsLeft,trnsLeft%26, first%26
        if isPrim(trnsLeft) and isPrim(trnsRight):
            tnum = str(first) + str(trnsLeft % 10) + str(first) + str(trnsRight % 10)
            print (first, tnum, prime1, tnum[::-1], prime2, tnum[::-1], sum(map(int, tnum)))
            sumn = sum(map(int, tnum))

        trnsLeft -= 1
        trnsLeft %= 26
        trnsLeft = chr((ord(tnum[10])) + ord("A"))

print sumn
