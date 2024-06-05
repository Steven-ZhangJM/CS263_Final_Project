

from itertools import permutations


def find_num():

    two_multiples_num = nums = range(0, 10001)

    for num in nums:
        two_doubles = set(map(lambda x: int(str(num) + str(x) + str(x) + str(num)), permutations(str(num))))

        if len(two_doubles) > len(two_multiples_num):
            two_multiples_num = two_doubles


    return min(two_multiples_num)

print(find_num())
