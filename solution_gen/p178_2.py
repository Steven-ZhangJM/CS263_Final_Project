


from math import sqrt

def pandigital(num):

    if sum(set(str(num)))!= 10:
        return False
    n = int(sqrt(num))
    for i in range(1,n+1):
        if num!= i*(n):
            return False
    return True

# we'll try to find a pandigital number until we've narrowed it down further
pandigital_numbers = []
for number in xrange(100000,100001):
    if number == int(str(number)):
        n = set(str(number))
        if pandigital(number) and len(n) == 10:
            pandigital_numbers.append(number)

num = 0
for i in pandigital_numbers:
    if int(str(i)[0]) + int(str(i)[1])!= int(str(i)[2]) and \
        int(str(i)[0]) + int(str(i)[3])!= int(str(i)[4]) and \
        int(str(i