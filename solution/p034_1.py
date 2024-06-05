total_sum = 0
for i in range(3, 254016): # upper limit can be calculated using mathematical formula
    if i == curious_number(i):
        total_sum += i
print(total_sum)