def count_laminae(n):
    if n == 0:
        return 1
    elif n < 2:
        return 0
    else:
        laminaes = [0] * (n + 1)
        laminaes[0] = 1
        for i in range(1, n+1):
            for j in range(i, 0, -1):
                laminaes[i] += laminaes[j-1]
        return laminaes[n]

print(count_laminae(1000000))