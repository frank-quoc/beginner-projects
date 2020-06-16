from random import randint

def dice_roll(sides):
    dice = randint(1, sides)
    return dice

if __name__ == '__main__':
    while True:
        print("How many sides would you like your dice to have?")
        sides = input("Enter 'q' to exit. ")
        if sides.lower() == 'q':
            exit()
        else:
            print("\nRolling...")
            print("You rolled a: " + str(dice_roll(int(sides))) + ".\n")