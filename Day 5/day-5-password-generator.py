#Password Generator Project
import random

# list_item
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#user_input
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def generate_random_number(limit):
  return random.randint(0, limit)

# string_item
letter_string = []
symbols_string = []
numbers_string = []
password_generated = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# def create_string(user_input, string_item, list_item):
#   for item in range(0, user_input):
#     random_number = generate_random_number(len(list_item))
#     string_item.append(list_item[random_number - 1])

# def create_password():
#   for item in letter_string:
#     password_generated.append(item)
#   for item in symbols_string:
#     password_generated.append(item)
#   for item in numbers_string:
#     password_generated.append(item)
#   for item in password_generated:
#     print(item, end = '')

# def init():
#   create_string(nr_letters, letter_string, letters)
#   create_string(nr_symbols, symbols_string, symbols)
#   create_string(nr_numbers, numbers_string, numbers)
#   create_password()

# init()

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
string_items = ['letter_string', 'symbols_string', 'numbers_string']

def create_string(user_input, string_item, list_item):
  for item in range(0, user_input):
    random_number = generate_random_number(len(list_item))
    string_item.append(list_item[random_number - 1])

def create_password():
  for item in letter_string:
    password_generated.append(item)
  for item in symbols_string:
    password_generated.append(item)
  for item in numbers_string:
    password_generated.append(item)
  random.shuffle(password_generated)
  for item in password_generated:
    print(item, end = '')

def init():
  create_string(nr_letters, letter_string, letters)
  create_string(nr_symbols, symbols_string, symbols)
  create_string(nr_numbers, numbers_string, numbers)
  create_password()

init()