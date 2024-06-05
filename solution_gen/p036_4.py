

# I used this answer:
# https://leetcode.com/problems/palindrome-number/solution/


def palindrome_in_binary(num):
    # this is an even palindromic integer in decimal
    if num < 10:
        return True

    # take modulus (remainder) and get a boolean
    rem = num % 10
    # take this as the integer to find the palindrome at
    integer = num // 10

    return rem == integer or palindrome_in_binary(integer)


def palindrome_in_dec(num):  # O(n)
    if(num < 10):
        return True
    if num % 10 == 0 and num >= 10:
        return False
    if (num % 10) == (num // 10) % 10:
        return True
    return palindrome_in_dec(num//10)


def sumOfPalindromes():  # O(n^2)
    # create a list with all the numbers:
    allNum = list(range(100000))
    # make a function that find's the sum of nums:
    listToFind = []  # list with all the palindromic numbers
    # find all the numbers:
    for i in allNum:
        # make a list with all the palindromic numbers:
        listToFind.append(str(i))
    # calculate the sum(i is the number):
    counter = 0
    for i in listToFind:
        # print(i)

        if palindrome_in_dec(int(i)):
            counter += int(i)
        if palindrome_in_binary(int(i)):
            counter += int(i)
    return counter


# print(sumOfPalindromes())
