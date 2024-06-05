

# O(n) time | O(n) space, where n is the size of the digits

def maximumPalindromeProduct(digits):
    if len(digits) == 3:
        nums = [int(x) for x in digits]
        return int((nums[0] * nums[1]) * nums[2])

    results = []
    for i in range(len(digits) + 1):
        if i > 1:
            a = int(digits[:i])
            b = int(digits[i:])
        else: # i == 1
            a = int(digits[0])
            b = 0
        
        result = maximumPalindromeProduct(digits=str(a + b))
        # if (n < i) return max
        if result < max:
            max = result

    return max

digits = '12356893'
# digits = '2315'
# digits = '1232456'
result = maximumPalindromeProduct(digits)
assert result == 9069

if result == 9069:
    print("Test 1 passed!")
else:
    print("Test 1 failed. Got {}".format(result))

# Time: O(n x 3)
# Space: O(n x 3)

