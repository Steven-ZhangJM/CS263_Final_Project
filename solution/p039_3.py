import math

def find_solutions(p):
    count = 0
    for a in range(1, p+1):
        for b in range(a, p-a+1):
            c_squared = p*p - (a*a + b*b)
            if c_squared >= 0 and int(math.sqrt(c_squared))**2 == c_squared:
                count += 1
    return count

max_count = 0
max_p = 0
for p in range(1, 1001):
    count = find_solutions(p)
    if count > max_count:
        max_count = count
        max_p = p

print(max_p)

#