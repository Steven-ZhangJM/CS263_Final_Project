def has_sum_greater_than_9(digits):
    for i in range(len(digits) - 2):
        if digits[i] + digits[i+1] + digits[i+2] > 9:
            return True
    return False

count = 0
for i in range(10**(20-3), 10**20):  # iterate over all 20-digit numbers
    digits = [int(x) for x in str(i)]  # convert number to list of digits
    if not has_sum_greater_than_9(digits):
        count += 1

print(count)