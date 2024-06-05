
from timeit import timeit


def num_digits_that_occur_more_than_on(max_n: int) -> int:
    # n % 10
    # loop through to get length of number in digits (e.g.: 25 has 1 3 5 which occurs 4 times)
    # nums = []
    # for i in range(1, max_n):
    #     n = str(i).rstrip("0")
    #     n = list(n)
    #     nums.append(len(n))

    nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    last_val = 1
    i = 0
    while True:
        num = str(last_val).rstrip("0")
        num = list(num)

        for num in num:
            nums[int(num)] += 1

        # set i to the first position of a number with a digit more than 3 times
        count_three_repetition =