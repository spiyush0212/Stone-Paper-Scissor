from random import randint
import time


# Variables


comp_won = 0
user_won = 0
tie_match = 0


# Functions


def game_match():

    global tie_match
    global comp_won
    global user_won

    user_w = int(input("\nSelect your weapon:\n0 for Stone\n1 for Paper\n2 for Scissors\n"))
    comp_w = randint(0, 2)
    print("Opponent Weapon = ", comp_w)

    who_won = "Tie"

    if user_w == 0:
        if comp_w == 0:
            who_won = "Tie"
        elif comp_w == 1:
            who_won = "PC"
        else:
            who_won = "User"
    elif user_w == 1:
        if comp_w == 0:
            who_won = "User"
        elif comp_w == 1:
            who_won = "Tie"
        else:
            who_won = "PC"
    else:
        if comp_w == 0:
            who_won = "PC"
        elif comp_won == 1:
            who_won = "User"
        else:
            who_won = "Tie"

    if who_won == "User":
        comp_won += 1
        # print("Who Won = ", who_won)
        print("Match Winner: You\n")
    elif who_won == "PC":
        user_won += 1
        # print("Who Won = ", who_won)
        print("Match Winner: Opponent\n")
    else:
        tie_match += 1
        # print("Who Won = ", who_won)
        print("Match Tied\n")


def main():
    print("\nSTONE PAPER SCISSORS\n")
    t = int(input("How many matches? "))

    while t > 0:
        game_match()
        time.sleep(2)
        t -= 1

    print("\nFINAL SCORE:\nUSER:PC:TIE\n", user_won, comp_won, tie_match)
    if comp_won > user_won:
        print("OPPONENT WON!")
    elif user_won > comp_won:
        print("YOU WON!")
    else:
        print("SERIES TIED")


# Game Starts


main()
