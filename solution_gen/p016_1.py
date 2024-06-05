

# solution learned from site : 
def sum_of_digits(number):
    return sum([int(i) for i in str(number)])

assert(sum_of_digits(3) == 3)
assert(sum_of_digits(1234) == 4)
assert(sum_of_digits(0) == 0)
assert(sum_of_digits(1) == 0)
assert(sum_of_digits(2) == 1)
assert(sum_of_digits(1024) == 10 + 1)
assert(sum_of_digits(2**1000) == 262144)

# using the power function 
number     = 2**1000
power      = format(number, "b")

res         = sum([int(i) for i in power])
assert(res == 262144)

# using bit manipulation and string operations 
number     = 2**1000
power      = format(number, "b")
res         = int(power, 2)
assert(res == 262144)
