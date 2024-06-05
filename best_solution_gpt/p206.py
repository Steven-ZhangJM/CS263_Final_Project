def find_special_number():
    # Start with the smallest number that, when squared, is close to the pattern.
    # The pattern suggests the number ends in 0, so the square root must end in 0.
    # We can start at 1010101010 and go up by increments of 10.
    num = 1010101010
    while True:
        square = str(num * num)
        # Check if the square matches the pattern 1_2_3_4_5_6_7_8_9_0
        if (square[0] == '1' and square[2] == '2' and square[4] == '3' and
            square[6] == '4' and square[8] == '5' and square[10] == '6' and
            square[12] == '7' and square[14] == '8' and square[16] == '9' and
            square[18] == '0'):
            return num
        num += 10

# Find and print the special number
special_number = find_special_number()
print(special_number)