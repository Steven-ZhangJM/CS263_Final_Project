

import math
from random import uniform as r
import matplotlib.pyplot as plt

rng = range(1, 10 ** 7)
p = (1 / math.sqrt(2))**2

plt.scatter([1, 2, 3, 4, 5], range(1, 10**7))
plt.grid()
plt.show()

t = []
for i in rng:
    
    a = r(0, 100)
    b = r(1, 100)

    h = math.sqrt(p * a**2 + p * b**2 - 2 * a**2 * p * b)

    if h >= 1:
        continue
    if a <= b:
        continue
    # c = a/1.1
    # c = a*1.1
    c = a*(1 + i**(j))
    
    
    #t.append(tuple([a, b, c, 1.1, math.sqrt(p * a**2 + p * b**2 - 2 * a**2 * p *