


def f1():
    a = 2345
    b = int(str(a) * 2)
    c = int(str(a) * 3)
    d = int(str(a) * 4)
    e = int(str(a) * 5)
    f = int(str(a) * 6)
    if (str(a) == str(b)
            and str(a) == str(c)
            and str(a) == str(d)
            and str(a) == str(f)):
        return a
    elif (str(a) == str(b)
    and str(a) == str(c) and str(a) == str(e)
    and str(a) == str(f)):
        return a
    elif (str(a) == str(b) and str(a) == str(d)
            and str(a) == str(f)
            and str(a) == str(e)):
        return a
    elif (str(a) == str(b) and str(a) == str(d)
    and str(a) == str(e) and str(a) == str(f)):
        return a
    elif (str(a) == str(b) and str(a) == str(c)
            and str(a) == str(d) and str(a) == str(f)):
        return a
    elif (str(a) == str(b) and str(a) == str(d) and str(a) == str(f) and str(a) == str(e)):
        return a
    else:
        return -1


print(f1())


"""
Find the sum of multiples of 3 or 5 below 1000

"""


def f2(x):
    total = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(f2(100))


"""
Return the number of strings of length n that can be formed using letters
 from a given string s.

You may use the lower case alphabet or uppercase alphabet of English
  as the 26 letters.
 """


def f3(s, n):
    if n == 0 or n == 1:
        return 1
    a = 0
    d = 0
    for i in range(len(s)):
        if s[i]!= a and ord(s[i]) >= 65 and ord(s[i]) <= 90:
            a = s[i]
            if s[i + 1]!= a and ord(s[i + 1]) >= 65 and ord(s[i + 1]) <= 90:
                a = s[i + 1]
            if s[i + 2]!= a and ord(s[i + 2]) >= 65 and ord(s[i + 2]) <= 90:
                a = s[i + 2]
            if s[i + 3]!= a and ord(s[i + 3]) >= 65 and ord(s[i + 3]) <= 90:
                a = s[i + 3]
            d += 1

    return d


print(f3('aBbGss', 4))


def f4(s):
    s = str(s)
    ans = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) == 1:
            ans += 1
    return ans


print(f4('abcde'))
