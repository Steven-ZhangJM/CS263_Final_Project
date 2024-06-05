


from collections import defaultdict
n = 10**7
primes = defaultdict(bool)
primes[2] = True
sum_value = 2
i=3
while i*i<=n:
    if primes[i]:
        for j in range(i*i,n,i):
            primes[j] = False
    i+=2
    for j in range(i*i,(i**2)-n-1,i):
        primes[j] = False
print("")
print("Answer: %d" % sum_value)