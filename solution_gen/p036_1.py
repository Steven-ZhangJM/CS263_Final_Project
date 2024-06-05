

def palindromic():
    ans = 0
    for i in range(1, 1000000):
        str_i = bin(i)[2:]
        str_i = '0' * (12 - len(str_i)) + str_i
        int_i = int(str_i, 2)
        if str_i == str_i[::-1]:
            ans += int_i
    return ans

print(palindromic())
