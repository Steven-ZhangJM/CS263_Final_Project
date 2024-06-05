decimal.getcontext().prec = 1000 # Set precision to 1000 for accurate results

total_sum = 0
for i in range(2, 101): # Iterate from 2 to 100
    decimal_sqrt = str(decimal.Decimal(i).sqrt())
    decimal_digits = decimal_sqrt.split('.')[1] # Get the first one hundred decimal digits
    total_sum += sum(int(digit) for digit in decimal_digits[:100]) # Calculate the digital sum

print(total_sum)
#