

#Solution
def compute():
    primes = get_top_ten(truncate_prime_numbers())
    #print(primes)
    prime = 4
    current_str = str(prime)
    while len(current_str)>=3 and prime<=99:
        prime, current_str = truncate_prime_numbers(n=prime), current_str[min(len(current_str)-1, 3):]
        #print(current_str, prime)
        if prime in primes:
            #print(prime, current_str)
            primes = primes+[prime]
            if len(primes)==11 and len(str(primes[10]))==3 and len(str(primes[8]))==3:
                return sum(primes)
    
            

def truncate_prime_numbers(n=11):

    str_n = str(n)
    for index in range(len(str_n)-2):
        yield int(str_n[index:index+2])
        
def get_top_ten(truncated):
    primes = list(filter(is_prime, truncated))
    primes = list(filter(lambda x : len(str(x))<6, primes))
    return primes
def is_prime(n):
    for j in range(2, int(n**0.5)+1):
        #print(j)
        if n%j==0 and n!=1:
            #print(n)
            return False
    return True

def all_primes(n=11):
    for i in range(2, n):
        prime = 0
        for j in range(len(str(i))):
            prime = prime + i%10 + int(i/10)
            if prime%10==0 and prime==0:
                pass
            else:
                yield i
                break
            #if prime==0:
             
            #else:
                #prime = prime-i
                #yield prime
                
        
    
if __name__ == "__main__":
    print(compute())