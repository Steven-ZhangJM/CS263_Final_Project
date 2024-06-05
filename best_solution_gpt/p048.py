# Python code to find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000

# Initialize the sum
series_sum = 0

# Calculate the sum of the series
for i in range(1, 1001):
    series_sum += i**i

# Get the last ten digits
last_ten_digits = str(series_sum)[-10:]

print(last_ten_digits)