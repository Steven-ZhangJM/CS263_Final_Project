
# Solution

"""
This problem can be solved by simply adding '0' as a starting digit to one of the smaller problems like 24 and 37.
Then, find the correct order of that particular smaller problem.
"""
from itertools import permutations


def solution():
    digits = list(range(0, 10))
    digit, perm = digits[0], ""
    counter = 0

    while digits:
        for index, digit_val in enumerate(digits):
            if index == 0:
                perm += str(digit)

            temp_permut = perm + str(digit_val)
            perm_index = []

            for num in temp_permut:
                perm_index.append(digits.index(int(num)))

            # print(digit_val, perm_index)
            digit = perm_index.pop(0)
            digits.remove(digit)

        counter += 1
    return perm


if __name__ == '__main__':
    print(solution())

"""
Runtime: 1248 ms, faster than 93.82% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.6 MB, less than 94.16% of Python3 online submissions for Permutation Sequence.
"""