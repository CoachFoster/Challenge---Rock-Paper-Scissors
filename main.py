#####
# Steps:
# (1) Use a random choice to make a computer move
# (2) Ask the user to enter a move
# (3) Print each moves
# (4) Determine the winner
#####

# set terminal output colors
pcred = "\033[91m"
pcgreen = "\033[92m"
pcyellow = "\033[93m"
pcblue = "\033[94m"
pcend = "\033[0m"

# import modules
import random
import time

# print intro
print(pcyellow + "ROCK, PAPER, SCISSORS" + pcend)
print(pcyellow + "---------------------" + pcend)
print(pcyellow + "This is a game of Rock, Paper, Scissors." + pcend)
print(pcyellow + "You will play against a computer component." + pcend)
print(pcyellow + "The computer will make it's choice first (in secret)." + pcend)
print(pcyellow + "Then you will be asked to make a choice." + pcend)
print(pcyellow + "The game will continue until you enter 'quit'." + pcend)
print()

print (pcyellow + "RULES:" + pcend)
print (pcyellow + "\tRock beats Scissors" + pcend)
print (pcyellow + "\tPaper covers Rock" + pcend)
print (pcyellow + "\tScissors cut Paper" + pcend)
print(pcyellow + "---------------------" + pcend)
print()

# initialize variables
valid_moves = ["rock", "r", "paper", "p", "scissors", "s"]
comp_score = 0
user_score = 0
done = False

# get player name
player_name = input(pcgreen + "Enter player name: " + pcend)
print()

# function to choices
def print_choices():
    print("\nComputer chose:\t", comp_choice)
    print(player_name + " chose:\t", user_choice)

# main game loop
while not done:
  comp_choice = random.choice(["rock", "paper", "scissors"])
  
  print (pcgreen + "Choose rock (r), paper (p), or scissors (s).")
  user_choice = input("Or enter 'quit' to exit: " + pcend)

  if user_choice.lower() == "quit":
    done = True
  elif user_choice.lower() not in (valid_moves):
    print(pcred + "Invalid user choice. You lose a point." + pcend)
    user_score -= 1
  elif comp_choice[0] == user_choice[0].lower():
    print_choices()
    print(pcblue + "Tie" + pcend)
  elif comp_choice[0] == "s" and user_choice[0].lower() == "r": #rock beats scissors
    print_choices()
    print(pcblue + player_name + " wins!" + pcend)
    user_score += 1
  elif comp_choice[0] == "r" and user_choice[0].lower() == "p": #paper beats rock
    print_choices()
    print(pcblue + player_name + " wins!" + pcend)
    user_score += 1
  elif comp_choice[0] == "p" and user_choice[0].lower() == "s": #scissors beats paper
    print_choices()
    print(pcblue + player_name + " wins!" + pcend)
    user_score += 1
  else:
    print_choices()
    print(pcblue + "Computer wins!" + pcend)
    comp_score += 1

  print()

# print game summary
print (pcgreen + "\nThe final score is ..." + pcend)
time.sleep(1)
print ("Computer: \t" + str(comp_score))
print (player_name + ": \t" + str(user_score))
print()

if user_score == comp_score:
   print (pcyellow + "It's a tie")
elif user_score > comp_score:
   print (pcyellow + "Congratulations! You are the winner. Humans rule!")
elif user_score < comp_score:
   print (pcyellow + "I'm sorry, you lost. Computers will take over the world!")
print("Thank you for playing.\nGoodbye." + pcend)