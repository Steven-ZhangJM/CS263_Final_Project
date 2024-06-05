def is_square(n):
    return n == int(n**0.5)**2

def find_smallest_xyz():
    z = 1
    while True:
        z2 = z*z
        for y in range(z + 1, 2*z):
            yz = y + z
            if is_square(yz):
                yz2 = yz*yz
                for x in range(y + 1, yz2 // (2*y) + 1):
                    if is_square(x + y) and is_square(x - y) and is_square(x + z) and is_square(x - z):
                        return x + y + z
        z += 1

# Find and print the smallest x + y + z
print(find_smallest_xyz())