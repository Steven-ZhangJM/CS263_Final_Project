def check_sum(n):
    for i in range(len(n)-2):
        if int(n[i:i+3]) > 9:
            return False
    return True

count = 0
for n in range(10**(20-1), 10**20):
    if str(n).lstrip('0') and check_sum(str(n)):
        count += 1

print(count)