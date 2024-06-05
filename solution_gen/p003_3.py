
def prime(x):
    """
    :param x: positive integer
    :return  
    """
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            print(f"the {i} is a prime {x}")
            break
    else:
        print(f"the {x} is not prime")


prime(13195)


















