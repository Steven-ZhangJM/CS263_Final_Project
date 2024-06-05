def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def concatenate_primes(prime1, prime2):
    return int(str(prime1) + str(prime2))

def find_lowest_sum_of_five_primes():
    lowest_sum = float('inf')
    for p1 in range(3, 1000000):  # start from 3 and go up to 1 million
        if not is_prime(p1):
            continue
        for p2 in range(p1 + 1, 1000000):
            if not is_prime(p2):
                continue
            concat = concatenate_primes(p1, p2)
            if not is_prime(concat):
                continue
            sum_of_five = p1 + p2
            for p3 in range(sum_of_five + 1, 1000000):  # start from the sum of p1 and p2
                if not is_prime(p3):
                    continue
                concat_p12_p3 = concatenate_primes(concat, p3)
                if not is_prime(concat_p12_p3):
                    continue
                for p4 in range(concat_p12_p3 + 1, 1000000):  # start from the concatenated result of p1, p2 and p3
                    if not is_prime(p4):
                        continue
                    concat_p123_p4 = concatenate_primes(concat_p12_p3, p4)
                    if not is_prime(concat_p123_p4):
                        continue
                    sum_of_five_concat = concat_p123_p4 + 1  # add the next prime to make it five primes
                    while not is_prime(sum_of_five_concat):
                        sum_of_five_concat += 1
                    if sum_of_five < lowest_sum:
                        lowest_sum = sum_of_five_concat

    return lowest_sum

print(find_lowest_sum_of_five_primes())

#