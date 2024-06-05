

def main():
    f1 = 'f1'
    f2 = 'f2'

    N = 100
    m = 0
    h = [x for x in range(1, N + 1)]

    # Using DFS
    # def helperDSF(nums, index, s):
    #     if index == len(nums):
    #         if s == 100:
    #             global m
    #             m += 1
    #             return
    #     else:
    #         s += nums[index]
    #         print(s, index)
    #         helperDSF(nums, index + 1, s)
    #         s -= nums[index]
    #         helperDSF(nums, index + 1, s)

    # Using DFS + BackTracking
    def helperBTracking(m, n):
        if m == 1:
            m += 1
            return 2, 1
        if n == 1:
            n += 1
            return 2, 1

        if m == n:
            m += 1
            return f1, f2
        elif m == n + 1:
            n += 1
            return f1, f2
        elif m == n + 2:
            m += 1
            return f1, f2
        elif m == n + 3:
            n += 1
            return f1, f2
        elif m == n + 4:
            n += 1
            return f1, f2
        elif m == n + 5:
            m += 1
            n += 1
            return f1, f2
        else:
            m += 1
            n += 1
            return (2, 1), (2, 2)

    ans = 0
    for m, n in helperBTracking(m, n):
        print(m, n)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
