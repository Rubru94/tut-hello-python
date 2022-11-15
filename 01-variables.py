# Variables. Naming convention: snake_case

# string
my_str_var = 'My str variable'
print(my_str_var)

# int
my_int_var = 4
print(my_int_var)

# bool
my_bool_var = False
print(my_bool_var)

# Concat vars 
print(my_str_var, my_int_var, my_bool_var)

my_int_to_str_var = str(my_int_var)
print(type(my_int_to_str_var))

print(my_str_var, my_int_to_str_var, my_bool_var)

# Length
print(len(my_str_var))
print('My str variable length:', len(my_str_var))

# Oneline variables. Carefully!
name, surname, age = 'Jonh', 'Smith', 34
print('Surname:', surname, '* Name:', name, '* Age:', age)

# input
first_name = input('What is your name: ')
print('User:', first_name)

# Change type
name = 20
age = 'Foo'
print('Surname:', surname, '* Name:', name, '* Age:', age)

# Python has Strong Dinamic Typing.
address: str = 'C/ Example'
address = 20
print(address)

'''
a = 5
b = "7"
print(a + b)  # ¡Error!
'''