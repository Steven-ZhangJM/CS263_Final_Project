

def FindSumOfDigits(n):
    temp = n
    sum = 0
    while temp > 0:
        sum += int(temp % 10)
        temp = int(temp/10)
    return sum 

if __name__ == "__main__":
    n = 100
    sum = 0
    while(n > 0):
        sum += FindSumOfDigits(n)
        n -= 1
    print sum