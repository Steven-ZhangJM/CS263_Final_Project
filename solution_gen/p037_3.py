

def number_sum():
    number = 1

    while True:
        for i in range(2,8):
            if i > 9:
                break

            while number >= 10:
                number = number // 10

            if is_prime(number):
                number = number*i

            if len(str(number)) < 4:
                break

    return number


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True
