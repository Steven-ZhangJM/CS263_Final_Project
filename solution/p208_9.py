```
import math

def robot_journey(length):
    return math.factorial(2*length-1) // (math.factorial(length) ** 2)

code_length = 70
print(robot_journey(code_length))