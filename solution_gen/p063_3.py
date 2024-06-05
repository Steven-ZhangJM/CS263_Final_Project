

from solutions.p0125_pythagoras.solution import power


def solve():
    ans = 0
    for i in range(9, 100000):
        pow_value = power(i, 50)
        if str(pow_value) == str(pow_value)[::-1]:
            ans += 1
            print(pow_value)
    return ans


if __name__ == '__main__':
    print(solve())
