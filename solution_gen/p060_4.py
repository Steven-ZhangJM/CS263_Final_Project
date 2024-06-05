

'''
Solution
--------------

'''


# The goal of this problem is to find the highest prime 
# in a series that can be broken from other series to make 
# a prime number.

import math

def nextprime(n):
    """
    Returns the smallest prime > than n.
    """
    while True:
        n = n + 1
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                break
        else:
            return(n)

def prime_series(s):
    """
    Takes in the number (s) and returns a list of all primes 
    in the series.
    """
    if s <= 2:
        return(prime_series(3))
    else:
        primes=[]
        for i in range(2, s):
            if s % i == 0:
                return(prime_series(s-1))
            else:
                primes.append(i)
                s = s - 1
        return(primes + prime_series(s))

def sum_divisors(c, e, f):
    """
    Returns the prime divisors of a number between e and f.
    """
    sum_lst = []
    for j in range(e, f+1):
        for i in c:
            if j % i == 0:
                sum_lst.append(i)
    return(sum_lst)

def check_if_prime(n):
    """
    Returns a boolean value depending on whether a number
    is prime or not.
    """
    if n <= 3:
        return(n in (2,3))
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return(False)
        return(True)

# The first question asks for the number of primes in
# a given range. Therefore, we must first obtain the prime limit.
n = nextprime(int(input())-1)

# A prime number is in range 1 to n (inclusive), but not n+1 to n+2.
# Therefore a list of primes <= than that range is needed.
my_primes = prime_series(n+1)
print(my_primes)
# If we can find n in a given range, it is prime
# We can see that our primes can cover a range up to
# n/2 because n is a multiple of 5:
print(my_primes)
# Since there are only a few values in my_primes that
# are factors of n, then n must evenly divide (n - 2),
# so we check whether n/2 is divisible by n
print(n % 2== 0)

# The key issue here is to determine whether to check for 
# the next highest prime. So, we need a lower bound for
# k to check with:
k = n-10
# If k is not in my_primes, then n must also be prime.
if k not in my_primes:
    print(k)
    print("not found")
# If k is not in my_primes, check our next highest prime:
if k not in my_primes:
    i = 0 
    lower_bounds_lst = []
    c = prime_series(n)
    while True:
        while (i % 2 == 0) and (i!= n):
            i += 1
        lower_bounds_lst.append(i)
        if i in my_primes == True:
            print(i)
            print("found")
        if i> k:
            break
        i += 2
print(len(lower_bounds_lst))

e = lower_bounds_lst[len(lower_bounds_lst)-2]
f = lower_bounds_lst[len(lower_bounds_lst)-1]
my_nums = []
for i in range(e, f):
    if i in lower_bounds_lst:
        my_nums.append(i)
e = lower_bounds_lst[len(lower_bounds_lst)-2]
f = lower_bounds_lst[len(lower_bounds_lst)-1]
my_nums = []
for i in range(e, f):
    if i in lower_bounds_lst:
        my_nums.append(i)

for i in range(len(my_nums)):
    sum_of_divisors = 0
    for j in range(e, f+1):
        if j % my_nums[i] == 0:
            sum_of_divisors += 1
    if int((f - e)/2) >= sum_of_divisors>= int((f-e)/2)-1:
        my_result = f-e+1

    

print(my_result)



