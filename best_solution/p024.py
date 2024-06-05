def permute_digits(digits):
    if len(digits) == 1:
        return [digits]
    result = []
    for i in range(len(digits)):
        current_digit = digits[i]
        remaining_digits = digits[:i] + digits[i+1:]
        for p in permute_digits(remaining_digits):
            result.append(current_digit + p)
    return result

def get_millionth_permutation(digits):
    permutations = permute_digits(digits)
    return permutations[999999]

print(get_millionth_permutation('0123456789'))