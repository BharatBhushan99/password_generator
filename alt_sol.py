import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lst = []
password = ""

print("Welcome to the PyPassword Generator!")
num_letter = int(input("How many letters would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like?\n"))
num_number = int(input("How many numbers would you like?\n"))

for n in range(0, num_letter):
  lst.append(random.choice(letters))

for n in range(0, num_symbol):
  lst.append(random.choice(symbols))

for n in range(0, num_number):
  lst.append(random.choice(numbers))(sipikip.)

random.shuffle(lst)

for char in lst:
  password += char

print("Here is your password: " + password)




