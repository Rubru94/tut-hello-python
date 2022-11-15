# Arithmetic operators

# Addition
addition = 16 + 5
print(addition)

# Subtraction
subtraction = 16 - 5
print(subtraction)

# Multiplication 
multiplication = 16 * 5
print(multiplication)

# Division
division = 16 / 5
print(division)

# Modulus
modulus = 16 % 5
print(modulus)

# Floor division
floor_division = 16 // 5
print(floor_division)

# Exponentation
exponentation = 5 ** 3
print(exponentation)

# Operation with str
# Python has Strong Dinamic Typing.
print('Hello' + 'World')
'''
print('Hello' - 'World') # TypeError: unsupported operand type(s) for -: 'str' and 'str'
'''
print('Hello' + str(45))
'''
print('Hello' + 45) # TypeError: can only concatenate str (not "int") to str
'''
print('Hello ' * 4)
'''
print('Hello ' * 2.5) # TypeError: can't multiply sequence by non-int of type 'float'
'''

# Comparison operators

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print('3' == 3) # this equality check between incompatible types; it will always return False

print('Hello' > 'Foo') # Alphabetic ASCII

# Logic operators

print(3 > 4 and 'Hello' > 'Foo')
print(3 > 4 or 'Hello' > 'Foo')
print(not(3 > 4 and 'Hello' > 'Foo'))
