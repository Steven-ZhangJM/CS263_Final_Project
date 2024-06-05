


def solve(target):
    """
    Solving this problem is really simple. For any multiples
    of both (3) and (5), we should add the target value.
    However, if the number is a multiple of both (3) or (5),
    we should only add the value if it is divisible by the target
    (which basically means that we only add a multiple for each possible
    value of the range).
    """
    sum_below_3_5 = 0
    sum_below_target_value = 0
    divisible_by_3 = set()
    divisible_by_5 = set()
    for value in range(1, target + 1):
        if value % 3 == 0:
            divisible_by_3.add(value)
        if value % 5 == 0:
            divisible_by_5.add(value)
        if (value % 3 == 0 and value % 5 == 0) or (value % 3 == 0 and value % 5!= 0) :
            sum_below_3_5 = sum_below_3_5 + value

        if (value % 3!= 0 and value % 5 == 0) or (value % 3 == 0 and value % 5!= 0):
            sum_below_target_value = sum_below_target_value + value
    list_of_multiples = divisible_by_3.union(divisible_by_5)
    multiples_to_sum = list_of_multiples.difference(set([3, 5]))
    return sum_below_3_5 + sum_below_target_value + sum(multiples_to_sum)


print(solve(1000))
