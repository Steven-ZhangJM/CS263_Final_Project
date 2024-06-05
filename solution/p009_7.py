def pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_triplet_sum_to_1000():
    for a in range(1, 1000//3+1):  # start from 1 and go up to the maximum possible value of a
        for b in range(a+1, (1000-a)//2+1):  # b should be greater than a and less than c
            c = 1000 - a - b
            if pythagorean_triplet(a, b, c):
                return a * b * c

print(find_triplet_sum_to_1000())