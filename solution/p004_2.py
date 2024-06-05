max_palindrome = 0
for i in range(100, 999):
    for j in range(i, 999):
        if check_palindrome(i, j) and i*j > max_palindrome:
            max_palindrome = i*j

print(max_palindrome)