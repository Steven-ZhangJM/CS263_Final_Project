
import time
def perm_cube_five(a,b,c,d,e):
    def is_square(num):
        #Checks if num is a perfect square
        quot = num/2
        if num<0:
            return False
        if quot == 1:
            return False
        while quot > 0:
            if num%quot == 0:
                return True
            else:
                quot = quot - 1
    #Converts strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    #Checks if a number in the base 10 system is a permutation of a number in the base 10 system or its permutations are cubes
    def is_perm_cube(num):
        #Converts the digit that appear in the cube at least twice to their index in the base 10 system
        #If the number has no digits in the base 10 system more than twice it is not a permutation of its digits
        val = 0
        while num >= 10**val:
            num = num%(10**(val+1))
            val = val + 1
        if num == 6 or num == 7:
            return False
        else:
            #Checks to see which digits of a number in the base 10 number are permutations of each other
            for i in range(0,9):
                for j in range(0,9):
                    if (i!= j) and (str(i) + str(j) in str(num)):
                        return False
            return True
    #Checks to see if a number is a permutation of the base 10 system
    def is_perm(num):
        if len(str(num)) == 1:
            return True
        num = str(num)
        for i in range(0,len(num)-1):
            if num[i] > num[i+1]:
                return False
        return True
    #Checks if a number is a permutation of 2 other numbers in a certain permutation of the base 10 system
    def check_perm(num,num2,num3,num4):
        num = str(num)
        num2 = str(num2)
        num3 = str(num3)
        num4 = str(num4)
        for i in range(0,len(num2)-1):
            if (num2[i] > num2[i+1] or num2[i]<num2[i+1]) or (num3[i] > num3[j+1] or num3[i]<num3[j]):
                return False
        for i in range(0,len(num3)-1):
            if (num3[i] > num3[i+1] or num3[i]<num3[i+1]) or (num4[i] > num4[i+1] or num4[i]<num4[i+1]):
                return False
        return True
    #Finds the largest possible cube and the largest possible permutation of that cube
    def find_perm(val):
        temp = cube[0]
        for i in range(1,len(cube)):
            if (cube[i] > temp):
                temp = cube[i]
        temp2 = perm[0]
        for j in range(1,len(perm)):
            if (perm[j] > temp2):
                temp2 = perm[j]
        return temp2, temp
    #Finds the smallest numbers permutations of their cubes and their largest permutations of their cubes
    def perm_three(val):
        temp = ''
        if is_sq(val) and is_perm_cube(val):
            return val
        else:
            for i in range(0,9):
                for j in range(i+1,10):
                    temp2 = val.copy()
                #Replaces i and j digits as well as the digit 2^(j), 2^(j+1), and 2^(j+2) with j
                    for k in range(0,9):
                        temp = temp + str(k)
                        temp2 = temp2.replace(str(k),str(i))
                        temp2 = temp2.replace(str(2**(j)),str(j))
                        temp2 = temp2.replace(str(2**(j+1)),str(j+1))
                        temp2 = temp2.replace(str(2**(j+2)),str(j+2))
                        #Checks if the permutation cube can be multiplied by itself to increase permutations, e.g. 2^(j+1) = j becomes 2^(j+2) = j+1
                        if is_perm_cube(temp2) and is_perm(val) and check_perm(val,j,2**(j+1),2**(j+2)):
                            cube.append(temp2)
                            perm.append(j)
                            i2, j2 = find_perm(j)
                            i2, j2 = find_perm(j2)
                            if j2 < i2:
                                cube.remove(temp2)
                                perm.remove(j)
                                return val
                            temp2 = ''
                            return val
                            break
                            
    #Checks to see if a number is a permutation of its cube
    def is_sq(num):
        num = str(num)
        for i in range(0,10):
            if (i**3)%10 == (num%(i**3)) or (i**3)//10!= num//(i**3):
                return True
        return False
    #finds a cube with the smallest permutations of two cubes
    def perm_four(val):
        temp = 0
        if is_sq(val) and is_perm_cube(val):
            temp = val
            for i in range(1,6):
                for j in range(i+1,6):
                    temp2 = val.copy()
                    for k in range(0,9):
                        temp2 = temp2.replace(str(k),str(i))
                        temp2 = temp2.replace(str(2**(j-1)),str(j))
                    if is_perm_cube(temp2) and is_perm(temp) and check_perm(temp,i,2**(j-1),2**(j)):
                        cube.append(temp2)
                        perm.append(i)
                        i2, j2 = find_perm(i)
                        i2, j2 = find_perm(j2)
                        if i2 < j2:
                            cube.remove(temp2)
                            perm.remove(j)
                            return val
                            break
                        temp2 = ''
                        return val
                    temp = 0
        else:
            return val 
    #function of the recursive algorithm
    def recursion(val):
        a = perm_three(val) #Finds largest permutation of its digits
        while len(a)!= 0: #Checks that a cube doesn't repeat itself or its permutations
            if a == cube[0]:
                return cube[0]
            else:
                val = a
                cube.append(val)
                a = perm_three(val)
        a = perm_four(val) #Finds smallest permutation of its digits
        if a!= 0:
            return a
        else:
            return 0
    cube = [] #list of all cubes, to find a cube with the smallest permutations
    perm = [] #list of the digits from each cube, to find the smallest permutation of its digits
    a = recursion(start)
    if a == 0:
        return start
    else:
        return a