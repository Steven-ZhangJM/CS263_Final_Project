

def check_sum(number):
    str_n = str(number)
    sum_number = sum(int(i) for i in str_n)
    return sum_number == number


def problem26():
    for number in range(101, 100000000):
        if check_sum(number):
            return number

print(problem26())