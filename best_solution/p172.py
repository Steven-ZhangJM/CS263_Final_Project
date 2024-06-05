import math

def count_numbers():
    total = 0
    for i in range(10**(18-3)):
        n = str(i)
        if len(n) == 18 and any(count > 3 for count in [n.count(str(j)) for j in range(10)]):
            continue
        total += 1
    return total

print(count_numbers())