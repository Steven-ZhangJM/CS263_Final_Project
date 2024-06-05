
import time
from decimal import getcontext, Decimal


# Time to solve: 1.06s
def solve_1():
    result = 0
    decimal_number_limit = 1000000
    bin_number_limit = 12
    bin_number_to_decimal = ["0", "1", "10", "11", "100", "101", "110", "111"]
    # we can increase the limits, but it's too heavy for our memory

    for i in range(1, bin_number_limit - 2):
        decimal_number = Decimal(i).to_integral_value() * 10

        # no need to divide the values since they'll always be integers
        for bin_number in bin_number_to_decimal:
            binary_number_as_str = bin(i)
            binary_number_as_str = bin_number_as_str.replace("0b", "")
            # if the resulting string doesn't have a leading 0, we need to add it
            binary_number_as_str = "0" + binary_number_as_str

            if binary_number_as_str == bin_number:
                # if the binary number is a palindrome, we multiply it with the int value + the digit value inside the integer
                # we have to remove leading zeros using bin_number_to_decimal
                result += decimal_number + int(bin_number)

    print(result)


# Time to solve: 1.01s
def solve_2():
    result = 0
    number_to_find = 1_000_000
    binary_number_limit = 12
    # here we can increase the limit since we can have more bit that base 2 value
    bin_number_to_decimal = ["0", "1", "10", "11", "100", "101", "110", "111"]

    for i in range(1, binary_number_limit):
        for bin_number in bin_number_to_decimal:
            if i == 2 ** i:
                if bin_number == bin(i)[2]:
                    result += bin_number + int(bin_number)
                else:
                    # the result is not necessary a palindrome
                    break
        if result >= number_to_find:
            break

    # here we need to remove leading zeros
    decimal_number = result % 10

    # since we need to print binary numbers in base 10, here we can also divide number to it
    divider_10 = abs(decimal_number * 2)
    print(int(divider_10) * -1)


solve_1()
solve_2()
