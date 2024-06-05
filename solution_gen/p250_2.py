

N = int(input())
sum = list()
for i in range(2, N + 1):
    temp_sum = i  # start the sum with just that integer
    for k in range(2, i ): # keep counting until reaching integer k
        temp_sum *= i  # multiply the current sum with the current number
        temp_sum -= k   # every time the sum is greater than or equal to the previous number, subtract the previous sum
        # keep going and add
        sum.append(temp_sum)  # the sum will always be positive with binary search (i.e., greater than or equal to)
print(sum[-16:])