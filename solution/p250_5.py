import math

def count_subsets():
    total_sum = sum(i**(i+1) for i in range(250251))
    result = 0
    remainder = total_sum % 250
    for i in range(250, -1, -1):
        if (remainder + i*(i+1)) % 250 == 0:
            result += math.comb(250, i)
            remainder -= i*(i+1)
        else:
            break
    return int((result * (250**16)) % (10**16))

print(count_subsets())