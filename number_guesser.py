import random

PlayersTries = 0

print("Welcome to the Number Guesser!")
print("I'm thinking of a number between 1 and 100.")

RandomNumber = random.randint(1, 100)

while True:
    try:
        PlayersNumber = int(input("Please input your number: "))
        PlayersTries += 1  # count the guess here
    except ValueError:
        print("Please enter a valid number!")
        continue  # go back to the start of the loop

    if PlayersNumber < RandomNumber:
        print("Uh oh, You guessed too low!")
    elif PlayersNumber > RandomNumber:
        print("Uh oh, You guessed too high!")
    else:
        # correct guess
        print(f"Congratulations! You guessed the correct number: {RandomNumber}")
        print(f"You completed it in {PlayersTries} tries!")
        break  # exit the loop

print(f"Congratulations! You guessed the correct number! It was {RandomNumber}.")
print(f"You completed it in {PlayersTries} tries!")