import random
import sys


def game_play():

        #the first choice input made by player
    your_choice = input("Pick a hand form(Rock,Paper or Scissors): ")

        #Possible options in the form of a list
    possibilities = ["rock", "paper","scissors"]
        #the computers random choice instruction
    comp_choice = random.choice(possibilities)

    print(f"(\nYou Chose {your_choice}, the computer chose {comp_choice}.\n")

    if your_choice == comp_choice:
                print(f"Both players selecetd {your_choice}. it is a tie!")

    elif your_choice == "rock":
                if comp_choice == "scissors":
                    print("Rock smashes scissors! You Win!")
                else:
                    print("paper covers rock, You lose!")

    elif your_choice == "paper":
                if comp_choice == "rock":
                    print("Scissors cuts paper! you lose.")
                else:
                    print("Rock smashes scissors, you lose.")
game_play()

game_is_on = True
continue_ = input("Would you like to continue?(Y)yes or (N)No.")
if continue_ == "Y":
    game_play()
elif continue_ == "N":
    game_is_on = False
    print("Game Over")


