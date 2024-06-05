

def four_digit_multiply (n):
    mult_dic = []
    for i in range(10,n+1):
        mult_dic.extend(i * int(str(i)))
    m = len(mult_dic)
    count = 0
    for i in range(m):
        count += mult_dic.count(mult_dic[i])
    print('There are {} numbers whose multiplicated product is'.format(count) + 'four digit strings without repeating digits.')

def five_digit_multiply(n):
    multiply = []
    for i in range(1000,n+1):
        multiply.extend(i * int(str(i)))
    multiply = set(multiply)
    count = 0
    for i in range(len(multiply)):
        count += multiply.count(multiply[i])
    print('There are {} numbers whose multiplicated product is'.format(count) + 'five digit strings without repeating digits.')

def main():
    four_digit