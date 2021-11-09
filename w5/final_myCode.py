from art import logo
import random
from os import system


def game():
    print(logo)
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = int(input("Choose a difficulty, 'easy' or 'hard': "))

    if difficulty == 'easy':
        guess_amount = 10
        print("You have 10 attemps to guess the number.")
    else:
        guess_amount = 5
        print("You have 5 attemps to guess the number.")

        theNumber = random.randint(1, 100)
        print("Pssst, the number is {theNumber}")

    while guess_amount != 0:
        guess = input("Make a guess: ")
        if guess = theNumber:
            print(f"You win the number was {theNumber}")
            guess_amount = 0
        elif guess >= theNumber:
            print("Too high")
            print(f"You have {guess_amount} attemps remaining.")
            guess_amount - 1
        else:
            print("Too low")
            print(f"You have {guess_amount} attemps remaining.")
            guess_amount - 1


system('clear|cls')
game()
