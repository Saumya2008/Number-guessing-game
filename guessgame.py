import random
print("Number guessing game.")
number = random.randint(1, 9)
chances = 0
print("Guess a number between 1-9: ")
while chances < 5:
    guess = int(input('Enter your Guess: '))
    if guess == number:
        print("Congratulations!! YOU WON.")
        break
    elif guess < number:
        print("Your guessed number is low, guess a higher number than ", guess)
    else:
        print("Your guess was too high, guess a number lower than ", guess)

    chances += 1
if not chances < 5:
    print("YOU LOSE!! The correct number was ", number)
