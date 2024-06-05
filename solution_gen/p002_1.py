
def fib_sum(n):
    a,b = 0,1
    while(b <= 4000000):
        num = (a+b)%2
        #print(num)
        if (num == 0):
            #print(a,b)
            return a+b
        a,b = b, num

ans = fib_sum(10)
print ('sum = ', ans)
