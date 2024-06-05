# Python code to find the count of n-digit positive integers which are also an nth power

count = 0
for n in range(1, 22):  # 22 is the upper limit since 9**22 is the largest 21-digit number
    for base in range(1, 10):  # Single digit base (1-9)
        if len(str(base**n)) == n:
            count += 1
print(count)