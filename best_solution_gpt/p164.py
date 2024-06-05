def count_numbers(length, sum_last_two, last_digit):
    if length == 1:
        return 1 if last_digit <= 9 else 0
    if (length, sum_last_two, last_digit) in memo:
        return memo[(length, sum_last_two, last_digit)]
    
    total_count = 0
    for digit in range(10):
        if sum_last_two + digit <= 9:
            total_count += count_numbers(length - 1, last_digit + digit, digit)
    
    memo[(length, sum_last_two, last_digit)] = total_count
    return total_count

memo = {}
total_20_digit_numbers = sum(count_numbers(20, 0, first_digit) for first_digit in range(1, 10))
print(total_20_digit_numbers)