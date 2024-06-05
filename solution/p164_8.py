```Python
def check_sum(n):
    for i in range(len(str(n)) - 2):
        if int(str(n)[i]) + int(str(n)[i+1]) + int(str(n)[i+2]) > 9:
            return False
    return True

count = 0
for n in range(10**20, 10**21): # we start from 10^20 because there are at least two digits
    if check_sum(n):
        count += 1
print(count)
```