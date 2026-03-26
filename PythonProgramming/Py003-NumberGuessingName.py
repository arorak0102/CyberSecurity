# Number Guessing Game

import random

print("Welcome to a python built number guessing game!")

# Generate random number
mysteryNumber = random.randint(1, 100)

lives = 5

while True:
    print(f"\nRemaining chances : {lives}")
    userGuess = int(input("Enter your guess : "))

    if userGuess == mysteryNumber:
        print(f"Nice One, the correct number is {mysteryNumber}")
    else:
        lives -= 1
        print(f"Remaining chances : {lives}")

        if userGuess > mysteryNumber:
            print(f"The number is smaller than {userGuess}\n")
        elif userGuess < mysteryNumber:
            print(f"The number is greater than {userGuess}\n")
        else:
            print("Wrong Input!")

    if lives == 0:
        print("No more chances left!\nGameOver!")
        break
