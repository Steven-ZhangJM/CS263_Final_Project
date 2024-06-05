
##################################################################################
# Solution
##################################################################################
def answer(n):
    """
    Find the 30th digit of the next number that contains at least 2 digits as follows:
    - the first 3 digits are 1, 1, and 2
    - the last 3 digits are 4, 4, and 6
    """
    digits = 3
    sum = 5

    n = str(sum)
    new_number, num = '', 0
    while len(new_number) < n:
       new_number += str(sum ** digits)
       digits += 1
       sum = int(num) + int(new_number)
    return new_number[-1]

print(answer(20))