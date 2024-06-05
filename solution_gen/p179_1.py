


def divisors(n):
    if 1 in n:
        return -1
    if n<0:
        return 0
    elif n==0:
        return 1
    divisors = set(range(1,1+n))
    for i in range(0,n//2):
        if divisors[i]!= 0:
            divisors.discard(divisors[i])
    if n%2 == 1:
        divisors.discard(1)
    return len(divisors)

tests = int(input())

for i in range(tests):
    print(divisors(int(input())))
