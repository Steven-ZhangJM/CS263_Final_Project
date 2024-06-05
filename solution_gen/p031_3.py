


def change(arr, k, n):
    """
    recursive function to find different ways to make n cents.
    use memoization to speed up the process
    """
    if k == 0:
        return 1
    if arr[k] == 0:
        return 0
    if k < 0:
        return 0
    if k < n:
        return 0

    res = 0
    for i in range(n+1):
        res += change(arr, k-i, i)
    return res


def main():
    """
    input example
    """
    arr = [1, 2, 5, 10, 20, 50, 100, 200]

    num_coins, total = 200, 0
    print("the number of ways to make", num_coins,
          "using the coins", arr, "is", change(arr, num_coins, total))

    num_coins, total = 200, 1
    print("the number of ways to make", num_coins,
          "using the coins", arr, "is", change(arr, num_coins, total))

    num_coins, total = 200, 5000
    print("the number of ways to make", num_coins,
          "using the coins", arr, "is", change(arr, num_coins, total))


if __name__ == '__main__':
    main()
