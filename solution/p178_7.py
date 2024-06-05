def count_pandigital_step_numbers(n):
    pandigital_step_numbers = set()
    
    for i in range(10**(n-1), 10**n):
        is_pandigital = True
        is_step_number = True
        
        str_i = str(i)
        
        for j in range(len(str_i) - 1):
            if abs(int(str_i[j]) - int(str_i[j+1])) != 1:
                is_step_number = False
                break
            
        for digit in range(10):
            if str(digit) not in str_i:
                is_pandigital = False
                break
        
        if is_pandigital and is_step_number:
            pandigital_step_numbers.add(i)
    
    return len(pandigital_step_numbers)

print(count_pandigital_step_numbers(40))
```

#