def same_digits(x):
    return sorted(str(x)) == sorted(str(2*x)) == sorted(str(3*x)) == sorted(str(4*x)) == sorted(str(5*x)) == sorted(str(6*x))

x = 1
while not same_digits(x):
    x += 1
print(x)