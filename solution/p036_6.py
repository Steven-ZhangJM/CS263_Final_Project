palindromic_numbers = set()
for i in range(1000000):
    if is_palindrome(i) and is_palindrome(decimal_to_binary(i)):
        palindromic_numbers.add(i)
print(sum(palindromic_numbers))