def smallest_number_with_divisors(modulo):
    prime_numbers = []
    number = 1
    i = 2

    # Function to check for primality
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        j = 5
        while j * j <= n:
            if n % j == 0 or n % (j + 2) == 0:
                return False
            j += 6
        return True

    # Generating prime numbers and calculating the result
    while len(prime_numbers) < 500500:
        if is_prime(i):
            prime_numbers.append(i)
            number = (number * i) % modulo
        i += 1

    return number

# Call the function with the given modulo
print(smallest_number_with_divisors(500500507))