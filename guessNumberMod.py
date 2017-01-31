import random

print('Hello. Welcome to the Guess The Number Game. What is your name?')
name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 42.')
secretNumber = random.randint(1, 42)

for guessesTaken in range(1, 13):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')

else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
