

def isPrime(n): 
    # Corner cases 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True

    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return False

    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6

    return True


if __name__ == "__main__":
    total = 0
    for i in range(1, 1000001): 
        isPrime(i)
        total = total + i
    print (total)