

import time
start_time = time.time()

import math

with open("p092_digits.txt") as f:
    digits = [int(i) for i in f.readlines()]

# Find the three numbers whose cubes sum to 0
total = 0
l = []
for i in digits:
    for j in digits:
        if i + j + total == 0:
            l.append(i*100 + j*10 + total)
    total += i
    l.append(i*100 + total)
    total += i

l = set(l)
while True:
    next = next(k for k, v in dict(Counter(str(i))
                                  for i in l).items() if v >= 5)
    if len(l) > 300:
        break
    l.remove(next)
    n = int(next)

print(n, time.time() - start_time)

#print(n)
