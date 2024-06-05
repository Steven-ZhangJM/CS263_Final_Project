```python
def almost_equilateral_triangles():
    max_perimeter = 1000000000  # one billion
    perimeter_sum = 0
    
    for a in range(1, max_perimeter // 3 + 1):
        for b in range(a, max_perimeter // 2 + 1):
            c = max_perimeter - a - b  # ensure the triangle is almost equilateral
            
            if abs(a - b) <= 1 and a + b > c:  # check if the sides are almost equal
                perimeter_sum += (a + b + c)
    
    return int(perimeter_sum)

print(almost_equilateral_triangles())
```