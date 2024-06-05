

__author__ = 'Dmitry Patashun'
__lcc_id__ = 201001729

"""
In Python, you can concatenate strings by adding them. Using multiplication, this is
helpful to see the difference between strings and its characters in the concatenated
strings
"""
# Print strings
x = 5 + 6
print(x)

"""
You can also add integers but can only have integers. Use int(), to convert between
integers and floats
"""

print(10 + 3.14)
# Print floats
print(2.5 + 2.5)

"""
The difference between two integers is that the float() function is able to convert
between the float and integer. If you do something like this, you will get an int.
"""

print(int(2.5 + 2.5))  # prints 5
print(2.5 + (int(2.5)))  # prints 12

"""
You can do this for strings too:
"""

print(5 + '6')
print(2 + stringoftext)
