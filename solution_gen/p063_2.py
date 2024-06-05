

import time
import math

def is_prime(number):
    if number <= 0 or number > 20:
        return False
    elif number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    
    n = int(number ** (0.5))
    fasts = []
    for a in range(4, n+1, 2):
        if number % a == 0:
            fasts.append(a)
            fasts.append(number//a)
    return 0 in set(fasts)

def gen():
    n=2
    while True:
        yield n
        n = n*2

def count_nums(gen_n):
    start_nums = 0
    total_nums = 0
    while True:
        start_nums += 1
        start_time = time.time()
        n = next(gen_n)
        if is_prime(n):
            total_nums +=1
        end_time = time.time()
        print(n)
        print(end_time - start_time)
        if total_nums > start_nums:
            if time.time() - start_time > 0.001:
                print('\n\n')
                return total_nums

if __name__ == '__main__':
    print(count_nums(gen()))