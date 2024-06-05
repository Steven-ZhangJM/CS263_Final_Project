import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n = 20000000
k = 1500000

coeff = binomial_coefficient(n, k)
print(sum([int(math.log(i)) for i in math.factorize(coeff)[0]]))