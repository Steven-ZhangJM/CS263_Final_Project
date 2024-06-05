

# Solution

a = 2**1000
digits_sum = 0

while a!= 0:
    digits = a%10
    digits_sum += digits
    a = a//10
print(digits_sum)