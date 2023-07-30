import art
import random

real_number = random.randint(1, 100)
guess_num = 0

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a diffivulty. Type 'easy' or 'hard':")
if level == "easy":
    guess_num = 10
else:
    guess_num = 5


def check_num(number):
    if number > real_number:
        print("Too high.")
    elif number < real_number:
        print("Too low")
    else:
        print(f"You got it! The answer is {real_number}")


print(f"the number {real_number} ")

print(f"You have {guess_num} attempts remaining to guess the number.")
while guess_num > 0:

    player_choice = int(input("Make a guess: "))
    check_num(player_choice)
    if (player_choice == real_number):
        break
    guess_num += -1

    if (guess_num == 0):
        print("You have run out of guesses, you lose!")
    else:
        print(f"You have {guess_num} attempts remaining to guess the number.")
