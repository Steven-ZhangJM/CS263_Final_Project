

import time

start = time.time()


def count_digit_powers_simple(n):
    sum = 0

    for i in range(10, (10**n) + 1):

        if (int(i**n) == i):
            sum += 1


    return sum


print(count_digit_powers_simple(4))

answer_simple_1 = count_digit_powers_simple(6)
answer_simple_2 = count_digit_powers_simple(8)
answer_simple_3 = count_digit_powers_simple(10)



def count_digit_powers_simple_v2(n):
    counter = 0

    for a in range(10, 10**n+1):

        str_a = str(a)

        if len(str_a) == n:
            for b in range(0, 10):

                if str_a[b] == str_a[n-1]:
                    if len(str_a) == 2:
                        counter += 1

                    else:
                        counter += (b**10) // 10**(n-1) * 10
                else:
                    break

    return counter


print(count_digit_powers_simple_v2(10))
print(count_digit_powers_simple_v2(8))

print("Program ended.")

print("Time: " + str(round(time.time() - start, 7)))


'''
def count_digit_powers_simple_v2(n):
    counter = 0

    for e in range(10):
        for i in range(10**(n-1), 10**n+1):
            number = 0
            for j in (range(1, n)):
                number += (10**j) * e * i**j

            if number % i == 0:
                counter += 1

    return counter



# Example with 4 digit numbers
answer_simple_4 = count_digit_powers_simple(3)
print(answer_simple_4)

'''
