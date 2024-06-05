
from timing import timed
myfunc1 = timed(factorial1)
myfunc2 = timed(factorial2)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
    
@timed
def factorial(n):
    if n ==0:
        return 1
    elif n ==1:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    myfunc1(100)
    myfunc2(100)
    print(myfunc1.timer, myfunc1.max)
    print(myfunc2.timer, myfunc2.max)