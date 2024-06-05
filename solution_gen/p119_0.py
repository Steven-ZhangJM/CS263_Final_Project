
def fibonacci_sequence(n):
    n1 = 0
    n2 = 1

    result = n2
    for i in range(n):
        result = n2 + n1
        n1 = n2
        n2 = result
    
    return result

answer = fibonacci_sequence(30)
print(answer) # answer = 3162653