e Python code to solve the problem:

```Python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def circular_prime(n):
    """Check if a number is a circular prime"""
    digits = [int(digit) for digit in str(n)]
    num_rotations = len(digits)
    for _ in range(num_rotations):
        if not is_prime(int(''.join(map(str, digits)))):
            return False
        digits = digits[1:] + [digits[0]]
    return True

count = 0
for i in range(2, 1000000):
    if circular_prime(i):
        count += 1

print(count)