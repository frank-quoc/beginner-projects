import random 

player = input("What is your name? ")

print("\nHello " + player + ", guess a number between 1 and 10.")

number =  random.randint(1, 10)

count = 5

while count > 0:
    print("\nPress 'q' to quit.")
    guess = input("Guess a number: ")

    if guess.lower() == 'q':
        exit()
    elif guess.isdigit():
        guess = int(guess)
        if guess == number:
            break
        elif guess > number:
            count -= 1
            print("You're number is too high. You have " + str(count) + " guesses left.")
        elif guess < number:
            count -= 1
            print("You're number is too low. You have " + str(count) + " guesses left.")
    else: 
        print("You didn't give me a number.")
        continue

if int(guess) == number:
    print("\nCongrats! You guessed " + str(number) + " correctly in " + str(5 - count) + " tries.")

if int(guess) != number:
    print("\nYou ran out of guesses. The number is " + str(number) + ".")