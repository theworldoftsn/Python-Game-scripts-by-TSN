# This is a Guess the Number game.

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well ,' + myName + ',I am thinking of a number between 1 and 20.')

for guessesTaken in range(1):
    print('Take a guess.') # Four spaces in front of "print"
guess = input()
guess = int(guess)

if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"
        guess = input()
        guess = int(guess)
if guess > number:
      print('Your guess is too high.')
      guess = input()
      guess = int(guess)
if guess == number:
   print()
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' +
guessesTaken + ' guesses!')

if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')