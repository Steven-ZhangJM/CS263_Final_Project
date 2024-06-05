
def find_sum_pair(n):
    arr = []
    r_arr = []
    for i in range(1,n+1):
        r_arr.append(i)
        arr.append(i)
    print(arr)
    print(r_arr)
    sum_1 = 0
    t = len(r_arr)
    z = len(arr)-1
    for i in range(t):
        sum_1 = sum_1 + int(r_arr[i])
    for i in range(t):
        for j in range(z):
            sum_2 = sum_2 + int(arr[j]) * int(arr[z])
            z = z - 1
        if sum_2 == n ** 2 + sum_1:
            print(arr[i])
            print(r_arr[z])
            break

find_sum_pair(2)
find_sum_pair(3)
find_sum_pair(4)
find_sum_pair(5)
find_sum_pair(6)
find_sum_pair