

"""

Note: 
    Assume the input is the solution of a problem in which there isn't any number which can only be a solution to two non-equal cubes. In other words, we only have to check whether the number that is permuted is a cube.
    Thus, we can solve this problem on a straightforward basis. We check if input number is a solution of any non-equal cube or not. 
    Now since the input can be a cube, we can directly use a for loop for this problem which is more efficient than any of the function of other python programming languages.

"""


def check(num):

    count = 0
    
    while num!= 0:
        temp_num = num
        count = count + 1
        num = temp_num % 10
        temp_num = temp_num // 10

    return count > 5


def get_cube(num):
    
    temp_num = num
    count = 0
    
    while temp_num!= 0:
        temp_num = temp_num % 10
        count = count + 1
        temp_num = temp_num // 10

    return count == 5



max_num = 0

for i in range(1, 99999):
    if check(i) == True or get_cube(i) == True:
        cube = abs(i)
        if cube > max_num:
            max_num = cube

print(max_num)
