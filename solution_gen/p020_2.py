

from math import factorial as fact
def sum_digits(n):
    '''
    Return sum of digits of a
    '''
    if type(n) is int:
        #return sum(map(int, list(str(n))))
        return sum([int(i) for i in str(n)])
    else:
        raise TypeError('n should be an integer')

def main():
    '''
    main function is to call sum_digits
    '''
    n = 100
    print(sum_digits(n))
    print(fact(100))

if __name__ == '__main__':
    main()
