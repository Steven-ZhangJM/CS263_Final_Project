

import time

def solution(limit):
    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    primes_idx = {prime: idx for idx, prime in enumerate(primes)}
    max_so_far = 0
    max_sum = 0
    max_prime = 0
    while True:
        if time_count(max_so_far + 1) < limit / 3:
            break

        if time_count(max_so_far + 1) == limit * 30 / 25:
            if max_sum == max_so_far:
                break

        new_primes = []
        last_prime = 0
        next_prime = 0
        while primes_idx.get(max_prime, 0) < last_prime + 2:
            next_prime = primes[primes_idx[next_prime]]
            last_prime = next_prime - 1
            if primes_idx.get(next_prime, 0) > limit:
                last_prime = next_prime - 1
                next_prime = primes[primes_idx[last_prime]]
                break
            new_primes.append(next_prime)

        next_prime = 0

        while primes_idx.get(next_prime, 0) < last_prime + 2:
            next_prime = primes[primes_idx[next_prime]]
            if primes_idx.get(next_prime, 0) > limit:
                last_prime = next_prime - 1
                next_prime = primes[primes_idx[last_prime]]
                break
            new_primes.append(next_prime)

        max_sum = max(max_sum,last_prime+1)
        max_prime = new_primes[-1]

        max_so_far = max_prime

    return max_prime

def time_count(t):
    return time.process_time() - t

if __name__ == '__main__':
    print(solution(1000000))
