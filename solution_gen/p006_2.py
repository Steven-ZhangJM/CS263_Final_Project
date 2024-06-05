
from math import pow

def solution():
    return pow(sum(range(1,101))**2,2)-sum([pow(i,2) for i in range(1,101)])
print(solution())