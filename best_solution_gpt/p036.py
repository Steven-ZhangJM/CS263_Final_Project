# Python code to solve the problem

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def sum_palindromic_numbers(limit):
    total_sum = 0
    for num in range(limit):
        if is_palindrome(num) and is_palindrome(bin(num)[2:]):
            total_sum += num
    return total_sum

# Find the sum of all numbers less than one million
# which are palindromic in base 10 and base 2
print(sum_palindromic_numbers(1000000))