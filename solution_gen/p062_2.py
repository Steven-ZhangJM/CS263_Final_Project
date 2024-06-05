
import itertools

number = set(range(1, 1000001))
tup = tuple(n for n in range(1, 1000))
for p, s in itertools.product(tup, tup):
    value = sum(int(n)**3 for n in str(p))
    if value not in number:
        number.remove(value)

print(number)
print(min(number))
