```Python
def check_sum(n):
    for i in range(len(str(n)) - 2):
        if int(str(n)[i]) + int(str(n)[i+1]) + int(str(n)[i+2]) > 9:
            return False
    return True

count = 0
for n in range(10**(20-1), 10**20):
    if check_sum(n) and n != 0:
        count += 1

print(count)
```