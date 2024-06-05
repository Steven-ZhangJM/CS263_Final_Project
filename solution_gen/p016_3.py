


def two_to_ten_thousand():
    sum = 0
    for i in range(2, 10):
        sum += (i ** 1000) % 1000
    return sum


assert two_to_ten_thousand() == 2, "Solution is wrong, please check your code"
print("You got 2 if test passed!")


