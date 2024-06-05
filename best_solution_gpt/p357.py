from sympy import isprime

def sum_of_special_numbers(limit):
    total_sum = 0
    for n in range(1, limit + 1):
        all_prime = True
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                if not (isprime(d + n // d) and isprime(n // d + d)):
                    all_prime = False
                    break
        if all_prime:
            total_sum += n
    return total_sum

# Set the limit to 100,000,000
limit = 100000000
print(sum_of_special_numbers(limit))