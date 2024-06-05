


import math


def primes(n):
    """Returns a list of primes, including 1."""
    result = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            n /= i
            result.append(i)
    if result[-1]!= n:
        result.append(n)
    return result


primes_lst = primes(1000000)

max_range = 0
max_sum = 0


def consecPrs(range_lst, primes):
    for num in range_lst:
        curr_sum = 0
        curr_primes = []
        for prime in primes:
            curr_sum = prime + num
            curr_primes.append(prime)
            curr_sum += prime
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_prime_lst = curr_primes[:]
            max_prime_lst.sort()
    print(f"The prime {max_prime_lst[0]} with a sum of {max_sum} is the most consecutive prime sum below one-million.")
    print(f"It can be written as the sum of {max_prime_lst[1:]}.")


list_num = 1
for prime in primes_lst[1:]:
    list_num += 1  # for easier printing
    if len(primes_lst[:list_num]) <= 7:
        consecPrs(range_lst=range(1, list_num), #range from 1 to (list_num -1) exclusive
                primes=primes_lst[:list_num])
        # range = 1 -> primes_lst[:list_num] inclusive
    else:


# print(f"The prime {max_prime_lst[0]} with a sum of {max_sum} is the most consecutive prime sum below one-million.")
# print(f"It can be written as the sum of {max_prime_lst[1:]}.")
