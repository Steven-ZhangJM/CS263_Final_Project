


from __future__ import print_function


def isPrime(x):
    if x%2 == 0:
        return False
    for i in range(3, int(x),2):
        if (x%i)== 0:
            return False
    return True

n=9
prime_list = []

for i in range(1, 10):
    for j in range(1, 10):
        s = str(i) + str(j)
        if isPrime(int(s)) and int(s) not in prime_list:
            prime_list.append(int(s))
            
print(len(prime_list))

"""
OUTPUT -

13
"""