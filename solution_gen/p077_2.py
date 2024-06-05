

# First we need to determine the primes
import time as time
start = time.time()
def sievePrimes(n): 
    
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    return prime
primes = sievePrimes(500000)

# the sum of each term is prime number - 1

# now the first condition is sum of prime is ten; for further we need to check if 5 + 7 is a prime and then we find only one option and move on to the next prime.

def primePairSum(n): 
    for i in range(len(primes)):
        for j in range(2, primes[i]+1):
                if (primes[i] / j + j) in primes:
                        return (primes[i], primes[i]/j + j)

ans = int(1)
primeSum = primePairSum(10*1000)
answer = []
print("prime", primeSum[0], "and ", primeSum[1])
count = 1

while True:
	if (primeSum[0] + count) in primes or count == 500000:
		ans += count
		count = 0
	count += 1
print("The answer is ", ans)
print("Runtime for the answer is: ", time.time() - start)