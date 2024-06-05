

from typing import List

def solve(n: int) -> int:
    cnt = 2
    count = 2
    for i in range(2, n):
        if count == i:
            cnt += 1
            count = 1
        else:
            count += i
        if cnt >= count + n:
            break
    return cnt
    

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solve(n))