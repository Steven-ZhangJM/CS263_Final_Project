


def sumEvenFibs(max):
    count = 0
    temp = 1
    first_num = 1
    second_num = 2

    while first_num <= max:
        if (first_num%2 == 0):
            temp = first_num
            count += first_num
        first_num = second_num
        second_num = temp
    
    return count

print(sumEvenFibs(4000000))
