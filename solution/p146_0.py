def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

total_sum = 0

for n in range(10, 150000001):
    numbers = [n*n + i for i in [1, 3, 7, 9, 13, 27]]
    
    if all(is_prime(num) for num in numbers):
        total_sum += n
        print(f"Found {n}")

print(f"Sum of all such integers n below 150 million is: {total_sum}")
#