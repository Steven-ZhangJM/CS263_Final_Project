
import math
import numpy

p100Ways_mapping = {}
p100Ways_mapping[2] = 1
p100Ways_mapping[0] = 1

for i in range(0, 101):
    for j in range(i, 101):
        p100Ways_mapping[i + j] = p100Ways_mapping[i] + p100Ways_mapping[j]
# print(p100Ways_mapping)


def find_num_possible_numbers(a, b):
    if (a, b) in p100Ways_mapping:
        return p100Ways_mapping[(a, b)]
    elif (b, a) in p100Ways_mapping:
        return p100Ways_mapping[(b, a)]
    elif a == 0:
        return 0
    elif b == 0:
        return 0
    elif a == 1:
        return 1
    elif b == 1:
        return 1
    elif a == 0 and b == 1:
        return 0
    elif b == 2:
        return math.factorial(a-1) * math.factorial(b) * math.factorial(a)
    elif a == 2:
        return math.factorial(b-1) * math.factorial(b) * math.factorial(a)
    elif a == 3:
        return math.factorial(a-1) * math.factorial(b) * math.factorial(a)
    elif a == 4:
        return math.factorial(a-1) * math.factorial(b) * math.factorial(a)
    elif a == 5:
        return 6 * math.factorial(a - 5) * math.factorial(b) * math.factorial(a)
    elif a == 6:
        return 8 * math.factorial(a - 6) * math.factorial(b) * math.factorial(a)
    elif a == 7:
        return math.factorial(a-1) * math.factorial(b) * math.factorial(a)
    elif a == 8:
        return 9 * math.factorial(a - 8) * math.factorial(b) * math.factorial(a)
    elif a == 9:
        return 10 * math.factorial(a - 9) * math.factorial(b) * math.factorial(a)
    else:
        pass


# def main():
#     print(sum(numpy.arange(100).tolist()))
#
#
# if __name__ == "__main__":
#     main()
print(
    find_num_possible_numbers(2, 1) + find_num_possible_numbers(
        1, 1) + find_num_possible_numbers(1, 0)
)
print(math.factorial(2) * math.factorial(2) * math.factorial(2))
