
from typing import Generator
from math import sqrt

gen: Generator = (num for num in range(1, 100001) if len(list(filter(lambda x: not x % num, list(range((sqrt(num)) + 1))))) == 2)

for prime in gen:
    print(f"{prime} : {2 in filter(lambda x: not x % prime, list(range((sqrt(prime)) + 1)))}")

print(gen)


# or more concisely:

if 6 in (2 ** x if x > 1 else False for x in range((sqrt(100000)) + 1)):
    print(6)
else:
    print(False)
