def last_five_digits(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i % 1000000  # Keep more than 5 digits to handle trailing zeroes
        while result % 10 == 0:  # Remove trailing zeroes
            result //= 10
    return f"{result:05d}"[-5:]  # Format to ensure 5 digits are returned

# Example usage:
# print(last_five_digits(1000000000000))