


def solve(limit):
    def is_power(i, n):
        return (i * i) == (i ** n)

    count = 0
    for i in range(1, limit):
        if is_power(i, 5):
            count += 1

    return count


def main():
    a = 0
    for i in range(1, 10_000_000):
        a += solve(i)
    print(a)


if __name__ == "__main__":
    main()
