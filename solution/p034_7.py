max_number = 1000000
sum_of_curious_numbers = 0

for i in range(3, max_number):
    if i == sum_of_factorials(i):
        sum_of_curious_numbers += i

print(sum_of_curious_numbers)