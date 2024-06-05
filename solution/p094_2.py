*
```
def almost_equilateral():
    max_perimeter = 1000000000
    total_perimeter = 0
    
    for a in range(1, int(max_perimeter / 3)):
        for b in range(a+1, min(a + 7, max_perimeter // 2) + 1):
            c = max(a, b) + 1
            
            if abs(a - b) <= 1 and abs(b - c) <= 1:
                area = (a * b * c)**0.5
                perimeter = a + b + c
                
                if int(area) == area and perimeter <= max_perimeter:
                    total_perimeter += perimeter
    
    return total_perimeter

print(almost_equilateral())
```
**