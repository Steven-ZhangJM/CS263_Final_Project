
divisible = 2
prime = 3
while divisible!= 0:
    divisible = prime - 1
    prime = prime + 2
    while (divisible not in range(1,21)) or not divisible % prime:
        divisible = prime - 1
        prime = prime + 2
        if prime <= 11:
            break
print(prime)
