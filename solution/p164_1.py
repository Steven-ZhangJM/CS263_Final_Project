count = 0
for i in range(10**(20-1), 10**20):
    flag = True
    for j in range(len(str(i)) - 2):
        if int(str(i)[j]) + int(str(i)[j+1]) + int(str(i)[j+2]) > 9:
            flag = False
            break
    if flag:
        count += 1

print(count)