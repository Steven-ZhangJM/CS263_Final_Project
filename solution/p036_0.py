def is_palindromic(n):
    binary = bin(n)[2:]
    decimal = str(n)
    return (decimal == decimal[::-1] and binary == binary[::-1])

sum_of_palindromes = sum(i for i in range(1000000) if is_palindromic(i))
print(sum_of_palindromes)