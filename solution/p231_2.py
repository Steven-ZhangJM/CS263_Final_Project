import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

n = 20000000
k = 15000000

coeff = binomial_coefficient(n, k)
print(sum([int(math.log(i)) if i > 1 else 0 for i in math.factorize(coeff)]))