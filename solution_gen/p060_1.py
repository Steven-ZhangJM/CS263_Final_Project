

import time


start_time = time.time()

def get_prime_list():
    primelist = []
    for i in range(10, 5000):
        for j in range(10, 5000):
            number = i + j
            if number >= len(primelist):
                primelist.append(number)
                break
            else:
                if number not in primelist and any(number in l for l in primelist):
                    primelist.append(number)
            if len(primelist) >= 20:
                break
        if len(primelist) >= 20:
            break
    # return ",".join(map(str, primelist))
    return primelist

def generate_primes():
    primes = 1
    num = 3
    primes_list = []
    while len(primes_list) <= 5:
        for prime in primes_list:
            if prime in primes_list:
                continue
            if prime * prime > num:
                if primes not in primes_list:
                    primes_list.append(primes)
                break
            if prime % primes == 0 and (prime in primes_list or primes in num):
                break
            elif prime == num:
                print(primes_list)
        primes = primes + 1
        num = num + 2
        if primes == len(primes_list) + 1:
            primes = 3

print(generate_primes())
print(time.time() - start_time, "seconds.\n")# 3.0107016633551145 seconds



