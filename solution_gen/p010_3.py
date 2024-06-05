


def solution(n):
    start = 2
    primes = []
    while start < n:
        prime = True
        for p in primes:
            if start % p == 0:
                prime = False
                break
        if prime:            
            primes.append(start)
        start += 1
    sum = 0
    for num in primes:
        sum += num
    return sum


print(solution(2000000))
