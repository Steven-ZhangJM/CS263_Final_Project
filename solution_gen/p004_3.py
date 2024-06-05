
def max_palindrome(a, b):
    return int(str(a) * str(b))


if __name__ == "__main__":
    res = []
    a = 100
    b = 100
    while a <= 999 and b <= 999:
        temp_str = ''
        res.append((max_palindrome(a, b) - 1000, a * b))
        temp_str = str(a) + str(b) + temp_str
        for i in range(0, len(temp_str)):
            a1 = temp_str[i] + str(int(temp_str[i + 1]) * int(temp_str[i + 2]))
            a2 = int(temp_str[i]) + int(temp_str[i + 1]) * int(temp_str[i + 2])
            a3 = int(temp_str[i]) * int(temp_str[i + 1]) + int(temp_str[i + 2])
            if (int(a1) >= int(temp_str[i]) and int(a2) >= int(temp_str[i + 1]) and int(a3) >= int(temp_str[i + 2])):
                continue
            else:
                temp_str = temp_str[0:i + 2]
                break
        a = int(temp_str[0]) + 1
        b = int(temp_str[1]) + 1
    print(max(res))