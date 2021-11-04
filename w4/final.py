from art import logo
import random
from os import system


def getLogo():
    return logo


generator = {
    "letters": ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    "numbers": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    "symbols": ['!', '#', '$', '%', '&', '(', ')', '*', '+']
}

paswords = []


def generate(plist):
    '''Creates a password for the user by asking them
    how many lettes, symbols, and numbers then randomly
    shuffling'''

    print(getLogo())
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like?\n"))
    num_symbols = int(input("How many symbols would you like?\n"))
    num_numbers = int(input("How many numbers would you like?\n"))

    letters = "".join(random.choices(generator['letters'], k=num_letters))
    symbols = "".join(random.choices(generator['symbols'], k=num_symbols))
    numbers = "".join(random.choices(generator['numbers'], k=num_numbers))
    password = letters + symbols + numbers
    rpass = list(password)
    random.shuffle(rpass)
    plist.append("".join(rpass))

    again = input("Would you like to make another password?: ")
    if again.lower() == 'y':
        system('clear')
        generate(plist)


generate(paswords)

system('clear')
print("Here are your passwords!")
for password in paswords:
    print(password)
