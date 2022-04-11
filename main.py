import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lst = [letters, numbers, symbols]

password = ""
letter_count = 0
symbol_count = 0
number_count = 0

print("Welcome to the PyPassword Generator!")
num_letter = int(input("How many letters would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like?\n"))
num_number = int(input("How many numbers would you like?\n"))

while len(password) < num_letter + num_symbol + num_number:
  rand_choice = random.randint(0,2)

  if rand_choice == 0 and letter_count < num_letter:
    rand_letter_index = random.randint(0, len(letters) - 1)
    password += letters[rand_letter_index]
    letter_count += 1
  elif rand_choice == 1 and number_count < num_number:
    rand_number_index = random.randint(0, len(numbers) - 1)
    password += numbers[rand_number_index]
    number_count += 1
  elif symbol_count < num_symbol:
    rand_symbol_index = random.randint(0, len(symbols) - 1)
    password += symbols[rand_symbol_index]
    symbol_count += 1

print("Here is your password: " + password)




