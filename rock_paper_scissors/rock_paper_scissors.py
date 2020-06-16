from random import randint

choices = ['Rock', 'Paper', 'Scissors']

def pick(player=False):
    if player:
        try:
            choice = choices[int(input("Pick a number:\n1. %s\n2. %s\n3. %s\n" \
                % (choices[0], choices[1], choices[2]))) - 1]
            print("\nYou picked", choice + ".")
        except (IndexError, ValueError):
            print("You did not pick a valid entry. Please type 1, 2, or 3.\n")
            pick(True)
        else:
            return choices.index(choice) + 1
    else:
        comp = randint(1, 3)
        print("The computer chose " + choices[comp - 1] + ".\n")
        return comp

def find_winner(player, computer):
    winner = int(player) - int(computer)
    if winner == 0:
        print("Tie Game!")
    elif winner in (-2, 1):
        print("You Win!")
    else:
        print("You Lose!")

for __name__ in '__main__':
    while True:
        ply = pick(True)
        comp = pick()
        find_winner(ply, comp)

        leave = input("\nWould you like to quit? (y/n) ")
        if leave.lower() == 'y':
            exit()