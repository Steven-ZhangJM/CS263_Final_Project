def f(N):
    last_five = 0
    for i in range(5):
        last_five *= 10
        last_five += N % 10
        N //= 10
    return last_five

N = 1000000000000
print(f(N))