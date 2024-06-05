import math

def count_numbers():
    count = 0
    for i in range(10**(18-3)):
        n = str(i)
        if len(n) == 18 and max(map(n.count, '0123456789')) <= 3:
            count += 1
    return count

print(count_numbers())