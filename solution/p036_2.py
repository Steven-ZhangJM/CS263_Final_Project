*
```
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

palindromes = []
for i in range(1000000):  # less than one million
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):  # check palindromic in both bases
        palindromes.append(i)

print(sum(palindromes))
```
**