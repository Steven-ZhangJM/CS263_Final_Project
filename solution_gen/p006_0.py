

x = 1
for n in range(1,101):
    x = x + n ** 2
Sum_to_Square = x
x = 1
for n in range (1, 101):
    x = x + n
Sum_of_Squares = x**2
Difference = Sum_to_Square - Sum_of_Squares
print(f"The Sum difference between the squares of the first 100 natural numbers and the square of the Sum is {Difference}")


Sum_of_squares = sum(n * n for n in range(1, 101))
Sum_to_square = sum(n for n in range(1, 101)) ** 2
print(f"The sum difference between the Squares of the first 100 natural numbers and the square of the Sum is {Sum_to_square - Sum_of_squares}")
