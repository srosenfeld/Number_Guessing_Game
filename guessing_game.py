import random
import time

#Initializes the random integer to be guessed
answer = random.randint(1,50)

#Initializes user guess variable
guess = 0

#Initializes guess counter
counter = 0

print("Welcome to Guess My Number!")

while guess != answer:
    print("I'm thinking of a number between 1 and 50. What's my number?")
    guess = int(input())
    if guess > answer:
        print("Too high! Guess again!")
        counter += 1
    elif guess < answer:
        print("Too low! Guess again!")
        counter += 1
    else:
        counter += 1
        print("You guessed my number! Congratulations!")
        print("You tried " + str(counter) + " guesses.")
        time.sleep(10)
        break
