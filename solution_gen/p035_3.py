

import math

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

def rotations(x):
    x_list = list(str(x))
    rotated_list = []
    for i in range(1, len(x_list)+1):
        rotated_list.append(x_list[i-1])
    return rotated_list

def is_circular_prime(x):
    prime_list = []
    if is_prime(x):
        prime_list.append(x)
        rotation_list = rotations(x)
        for i in range(len(rotation_list)):
            next_rotation = rotations(int(rotation_list[i]))
            for j in range(len(next_rotation)):
                temp = rotation_list[i]+next_rotation[j]
                if temp < 10:
                    n_prime = int(str(temp)+str(temp+1)+str(temp+2)+str(temp+3))
                else:
                    n_prime = int(str(temp).zfill(3))+int(str(next_rotation[j]).zfill(3))
                if is_prime(n_prime):
                    prime_list.append(n_prime)
    return prime_list

total_max = 0
list_of_primes = set()

for i in range(100_000 + 1):
    if is_prime(i):
        list_of_primes.add(i)
        primes = is_circular_prime(i)
        for prime in primes:
            list_of_primes.add(prime)

    if len(list_of_primes) > total_max:
        total_max = len(list_of_primes)

print(f'Total number of circular primes below {100_000 + 1}: {len(list_of_primes)}.')