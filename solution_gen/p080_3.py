


import math

def iterative(x, limit, num, count, value, length) :
    x = x / limit
    x = int(x)
    if abs((x - number)) < 10**(-count-1) :
        return sum(value.ljust(length, '0'))
    else :
        for i in range (x//2+1):
            if i == 0:
                value, length = value.ljust(length, '0'), len(value)-1
            if i == x:
                value = value.lstrip('0')
                value = value.split()
                return sum(value)

            value = str(i*i) + value
            count+=3
            count+=2
            value = int(value)
            value+= (x-i)*9
            number = x-i
            value = str(value)
            if int(value) == number :
                length+=2
                continue

print("result :  ", iterative(6250000, int(math.sqrt(6250000)), 1, 0,'',0))