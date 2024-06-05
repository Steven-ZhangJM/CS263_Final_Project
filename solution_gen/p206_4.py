

def find_form_sqr(n):
    
    res = ""

    while n:
        res += str(n%10)
        n //= 10
    
    res = int(res)
    
    return int(str(res*res)[::-1])
    
    
    
def main():
    n = int(input("Input the number: "))
    print(find_form_sqr(n))
    
main()