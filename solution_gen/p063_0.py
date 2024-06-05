

import utils

DIFFERENCE_COUNT = 2
COMPARISON_COUNT = 10

def iterate():
    num_comparison_count = COMPARISON_COUNT
    num = 9
    result = 3 # We have a base and num = 9
    while num_comparison_count > 0:
        new_result = result / num
        if new_result.is_integer():
            result *= num
            num *= 9
        else:
            num += 1

        num_comparison_count -= 1

    return result

def answer(n):
    return utils.how_many_powers(n, iterate)

if __name__ == '__main__':
    input = utils.read_input(8, 2019, False)
    input.reverse()

    # input = utils.read_input(17, False)
    # input.reverse()

    # input = utils.read_input(2, False)
    # input.reverse()

    print(answer(input.pop()))
