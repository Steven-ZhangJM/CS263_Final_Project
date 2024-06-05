


from itertools import combinations_with_replacement

def fizz_buzz_numbers(n):
    """
    >>> fizz_buzz_numbers(10)
    1 4 6 8
    >>> fizz_buzz_numbers(20)
    1 4 2 5 16 17 34 5 64
    >>> fizz_buzz_numbers(50)
    1 4 2 7 5 14
    >>> fizz_buzz_numbers(100)
    1 4 2 2 7 44 714
    >>> fizz_buzz_numbers(200)
    1  4  2  2  7  5 17 35 34  7 14
    >>> fizz_buzz_numbers(1000)
    1  4  2  2  7  5 17 35 34  7 14  14  157 34
    """
    
    i = 10
    count = 0
    while i <= 10000:
        for combination in combinations_with_replacement(range(1,i+1)):
            #print(combination)
            count += int(str(i).replace('1