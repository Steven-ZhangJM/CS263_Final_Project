


def three_digit_sum(max_target: int, max_count: int = 10) -> int:
    counter = 0
    while counter <= max_count:
        total = sum_of_three_digit_sum(
            range(9, 10 + counter or 1, 10),
            range(9, 10 + counter or 1, 10),
            range(9, 10 + counter or 1, 10),
        )
        if total > max_target:
            counter += 1
        else:
            return counter


def sum_of_three_digit_sum(
    d1: range, d2: range, d3: range,
) -> int:
    total = 0
    for v1 in d1:
        for v2 in d2:
            for v3 in d3:
                total += is_valid([v1, v2, v3])
    return total


def is_valid(nums: list) -> bool:
    for num in nums:
        if _contains(nums, sum(nums) - num) and _contains(n