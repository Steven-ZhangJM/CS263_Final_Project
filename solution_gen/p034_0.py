


def factorial(n): return 1 if n == 0 else n * factorial(n - 1)


NUMBERS = {
     '0': 1,
     '1': 1,
     '2': 2,
     '3': 6,
     '4': 24,
     '5': 120,
     '6': 720,
     '7': 5040,
     '8': 40320,
     '9': 362880,
 }

def sum_digits(num):
    if num == 0: return 0
    elif num >= 10: return sum_digits(num // 10) + NUMBERS.get(str(num % 10))
    else: return NUMBERS.get(str(num))

if __name__ == '__main__':
    sum = 0
    for i in range(10, 1000):
       num = factorial(i)
       sum += sum_digits(i)
       #print(sum_digits(i))
    print(sum)

