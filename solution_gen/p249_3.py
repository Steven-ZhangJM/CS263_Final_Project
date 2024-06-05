


if __name__ == "__main__":
    # 1st solution: brute force
    s = input()
    p, n = 0, 5000
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 0:
            p += int(s[i])
        if p == int(s[i]):
            n -= int(s[i])

    if n > 0:
        print("Not found!")
    else:
        print(n)

    # 2nd solution: brute force
    # p = int(s[:4])
    # for i in range(5, 5000, 2):
    #     p = p+int(s[i])
    # print(p)

    # 3rd solution: with bit manipulation
    # p = 0
    # for i in range(4,5001):
    #     if (i & i-1) < 2:
    #         p += i
    # print(p)
