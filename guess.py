import random

print("Hello, there! What's your name?")
name = input()

print(f"Well, {name}, I'm thinking of a number between 1 and 100.")
# Creating a random integer between 1 and 100
randomNumber = random.randint(1, 100)

# The user is going to have only 7 guesses
for guessesTaken in range(1, 8):
    print("Take a guess.")
    # Transforming the guess into an integer, to compare with the random number
    guess = int(input())

    if guess < randomNumber:
        print("Your guess is too low.")
    elif guess > randomNumber:
        print("Your guess is too high.")
    else:
        # Break out of the loop, because the guess was correct
        break

if guess == randomNumber:
    # Transforming the integer into a string, to print it out
    print(f"Good job, {name}! You guessed my number in {str(guessesTaken)} guesses.")
else:
    print(f"Nope. The number I was thinking of was {str(randomNumber)}.")