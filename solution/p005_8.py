def find_smallest_divisible(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

n = int(input("Enter the number up to which you want to find the smallest positive integer: "))
print(find_smallest_divisible(n))