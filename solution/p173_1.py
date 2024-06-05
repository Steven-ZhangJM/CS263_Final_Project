import math

def num_laminae(n):
    if n < 1:
        return 0
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            total += 1
        else:
            j = math.ceil(n / i)
            total += j - i
    return total

print(num_laminae(1000000))
#