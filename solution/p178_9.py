import itertools

def is_pandigital(n):
    return set(str(n)) == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def is_step_number(n):
    return all(abs(int(digit1) - int(digit2)) == 1
               for digit1, digit2 in zip(str(n), str(n)[1:]))

count = 0
for length in range(10, 41):  # from 10 digits to 40 digits
    for pandigital_number in itertools.permutations('0123456789', length):
        step_number = int(''.join(pandigital_number))
        if is_pandigital(step_number) and is_step_number(step_number):
            count += 1

print(count)

#