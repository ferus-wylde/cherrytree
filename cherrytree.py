import random

print('''
Welcome to Café Cherrytree
__________________________

''')

chars = 'Red', 'Blue', 'Green', 'Purple', 'Yellow', 'Black', 'White', 'Pink', 'Silver', 'Gold',
chars_2 = 'Table', 'Door', 'Cat', 'Dog', 'Camel', 'Sheep', 'Duck', 'Badger', 'Fox', 'Shark', 'Fish' 
numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' 
numbers_2 = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' 

number = input('''Table for how many?
''')
number = int(number)

print('\n')

length = input('''How many courses?
''')
length = int(length)

print('\n')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
    password += random.choice(chars_2)
    password += random.choice(numbers)
    password += random.choice(numbers_2)
  print(password) 
  
  print('\nBon Appetit!')

  print('\n')
