


def solution(a, b):
    maxi = 0
    for i in range(a, b + 1):
        res = list(str(i))
        sumRes = sum(int(i) for i in res)
        if sumRes > maxi:
            maxi = sumRes
    print(maxi)
    return maxi


print(solution(1, 100))
