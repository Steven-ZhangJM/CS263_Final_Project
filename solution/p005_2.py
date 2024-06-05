*
```
def find_lcm(a, b):
    """Calculate the least common multiple (LCM) of two numbers"""
    def gcd(x, y):
        """Calculate the greatest common divisor (GCD) of two numbers"""
        while(y):
            x, y = y, x % y
        return x

    lcm = abs(a*b) // gcd(a, b)
    return lcm

def find_smallest_lcm(n):
    """Find the smallest positive number that is evenly divisible without any remainder by all of the numbers from 1 to n"""
    def find_gcd(x, y):
        """Calculate the greatest common divisor (GCD) of two numbers"""
        while(y):
            x, y = y, x % y
        return x

    smallest_lcm = 1
    for i in range(2, n+1):
        smallest_lcm = find_gcd(smallest_lcm, i)

    return smallest_lcm

n = 20
smallest_lcm = find_smallest_lcm(n)
print("The smallest positive number that is evenly divisible without any remainder by all of the numbers from 1 to", n, "is:", smallest_lcm)
```
**