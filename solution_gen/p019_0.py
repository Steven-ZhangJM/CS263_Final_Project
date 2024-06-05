

from calendar import monthrange, weekday


def main():
    s = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    y = 1901
    tot = 0
    m = 7 # the monday of the first of the month
    x = (y, 1)
    # while a leap year, if a year ending on a leap year is reached
    while y < 2001:
        # check if not a leap year, if so increase y by one
        if not y % 400 == 0 or not y % 100 == 0:
            y += 1
            continue
        # if a leap year, increase x by one
        x = (x[0] + 1, x[1] + 1)
        tot += 7 # the number of days in month m
        for i in range(x[1], 13):
            m = (m + s[i] + sum(y > j for j in (x[0],x[1])) - (y <= x[0])) % 7
        m = (m + s[x[1]] if x[1] + s[x[1]] < m else m)
    print(tot)

if __name__ == "__main__":
    main()
