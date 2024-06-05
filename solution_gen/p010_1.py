


def sumofprimes(upperlimit):
    sum = 2

    print("Primes from 2 to ", upperlimit, ": ", end="")

    for i in range(3, upperlimit, 2):
        prime = True # Initialize as true so that
        for n in range(3, i, 2):
            if i % n == 0:
                prime = False
        if prime:
            print(i, ",", end="")

            sum += i  # Add the ith prime number
            print(sum, end="")

    print(sum)
    return


def main():
    sumofprimes(2000000)
    return


# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
