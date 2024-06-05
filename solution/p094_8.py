def almost_equilateral_triangles():
    total_perimeter = 0
    for a in range(1, 1000001):  # iterate over all possible side lengths
        for b in range(a-1, a+2):  # two sides are equal to a
            c = max(3, a + abs(a - b))  # third side differs by no more than one unit
            if (a + b > c) and (c > abs(a - b)):  # check if it's a triangle
                area = (a * (b + c) - (0.5 * (abs((2*a*b) + (2*a*c) + (2*b*c))))) / 4.0
                if area == int(area):  # check if the area is an integer
                    total_perimeter += a + b + c
    return total_perimeter

print(almost_equilateral_triangles())