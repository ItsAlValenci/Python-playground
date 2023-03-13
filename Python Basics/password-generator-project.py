import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

input("Welcome to RandWords password Generator!\nPress ENTER to start")
num_letters = int(input("\nHow many letters would you like in your password?\n")) 
num_symbols = int(input(f"\nHow many symbols would you like?\n"))
num_numbers = int(input(f"\nHow many numbers would you like?\n"))

input("press ENTER to generate")

password_lst = []

for char in range(1, num_letters + 1):
  password_lst.append(random.choice(letters))

for char in range(1, num_symbols + 1):
  password_lst += random.choice(symbols)

for char in range(1, num_numbers + 1):
  password_lst += random.choice(numbers)

print(f"Your list of options is: {password_lst}")
random.shuffle(password_lst)

password = ""
for char in password_lst:
  password += char

print(f"\nYour new random password is: {password}")