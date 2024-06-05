

# A function that takes as a parameter a list and returns
# True if the list contains elements with equal digits.
#
# def sameElements(l):
#     if len(l)!= len(set(l)): return False
#     for i in range(0, len(l)):
#         if not all(k in l[:i] for k in l): return False
#     return True


def sameElements(liste):
    return len(set(str(i) for i in liste)) == len(liste)


for i in range(1, 99):
    if sameElements(list(range(0, i))):
        print(i)
        break
