# Python code to calculate the sum of multiples of 3 or 5 below 1000
sum_of_multiples = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(sum_of_multiples)