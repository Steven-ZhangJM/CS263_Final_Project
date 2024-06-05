def heron(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def check_integral_area(a, b, c):
    area = heron(a, b, c)
    return area.is_integer()

perimeter_sum = 0
limit = 1000000000

for side in range(2, limit//3 + 1):
    for diff in [-1, 1]:
        a = side
        b = side
        c = side + diff
        if check_integral_area(a, b, c):
            perimeter = a + b + c
            if perimeter < limit:
                perimeter_sum += perimeter

print(perimeter_sum)