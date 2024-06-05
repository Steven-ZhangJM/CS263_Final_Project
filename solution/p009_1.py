def pythagorean_triplet_sum(a, b, c):
    return a + b + c

def find_pythagorean_triplet(sum):
    for a in range(1, sum // 3 + 1):
        for b in range(a, (sum - a) // 2 + 1):
            c = sum - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

# Find the product abc
sum = 1000
product = find_pythagorean_triplet(sum)
print(product)

#