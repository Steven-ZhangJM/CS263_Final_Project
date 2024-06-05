)
n = 250250
count = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        sum_val = 0
        for k in range(1, j+1):
            if (k**k) % i == 0:
                sum_val += k**k
        if sum_val % i == 0:
            count += 1

print(f"