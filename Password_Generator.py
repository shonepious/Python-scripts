import string
import secrets

length = int(input("Enter password length: "))

print('''Choose your character set for the password:
         1. Numbers
         2. Special characters
         3. Letters (Uppercase)
         4. Letters (lowercase)
         5. Save''')

characters = ""
upperLetters = string.ascii_uppercase
lowerLetters = string.ascii_lowercase
numbers = string.digits
specialChars = string.punctuation


while True:
    choice = int(input("Pick a number "))

    if choice == 1:
        characters += numbers

    elif choice == 2:
        characters += specialChars

    elif choice == 3:
        characters += upperLetters

    elif choice == 4:
        characters += lowerLetters

    elif choice == 5:
        break

    else:
        print("Pick from the options given!")

password = []
for i in range(length):
    result = secrets.choice(characters)
    password.append(result)
print("Your password is " + "".join(password))
