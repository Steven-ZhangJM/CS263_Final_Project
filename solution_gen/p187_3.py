



def divisorCases(n):
    primes = []
    count = 0
    for i in range(1,n):
        if n%i!= 0:
            continue
        else:
            j = 1
            while (n/i)%j == 0:
                if j not in primes:
                    primes.append(j)
                if i not in primes and i*i!= j and i**2!= j:
                    primes.append(i)
                j += 1     
    primes.sort()
    primes.insert(0,primes[0])
    primes.insert(0,primes[1])   
    return len(primes)

if __name__ == '__main__':
    
    # numPrime = 2
    numPrime = 3
    results = []
    for i in range(2,10**8):
        res = divisorCases(i)
        if res == numPrime:
            results.append(res)
    print(sum(results))
