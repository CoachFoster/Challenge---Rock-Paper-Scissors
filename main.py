###
# Steps:
# (1) Use a random choice to make a computer move
# (2) Ask the user to enter a move
# (3) Print each moves
# (4) Determine the winner
###

# set terminal output colors
pcred = "\033[91m"
pcgreen = "\033[92m"
pcyellow = "\033[93m"
pcblue = "\033[94m"
pcend = "\033[0m"

import random

print("ROCK, PAPER, SCISSORS\n")

valid_moves = ["rock", "r", "paper", "p", "scissors", "s"]
comp_score = 0
user_score = 0

def print_choices():
    print("\nComputer chose: " + comp_choice)
    print("You chose: " + user_choice)
    print()

while True:
  comp_choice = random.choice(valid_moves)
  print (pcgreen + "Choose rock (r), paper (p), or scissors (s).")
  print ("Or enter 'quit' to exit: " + pcend)
  user_choice = input()

  if user_choice.lower() == "quit":
    break
  elif user_choice.lower() not in (valid_moves):
    print(pcred + "Invalid user choice. You lose a point." + pcend)
    user_score -= 1
  elif comp_choice[0] == user_choice[0].lower():
    print_choices()
    print("Tie")
  elif comp_choice[0] == "r" and user_choice[0].lower() == "p": #paper beats rock
    print_choices()
    print("You win!")
    user_score += 1
  elif comp_choice[0] == "p" and user_choice[0].lower() == "s": #scissors beats paper
    print_choices()
    print("You win!")
    user_score += 1
  elif comp_choice[0] == "s" and user_choice[0].lower() == "r": #rock beats scissors
    print_choices()
    print("You win!")
    user_score += 1
  else:
    print_choices()
    print("Computer wins!")
    comp_score += 1

  print()

print (pcyellow + "\nThe final score is:")
print ("\tComputer: " + str(comp_score))
print ("\tPlayer:   " + str(user_score))
print()

if user_score == comp_score:
   print (pcgreen + "It's a tie")
elif user_score > comp_score:
   print (pcgreen + "Congratulations! You are the winner. Humans rule!")
elif user_score < comp_score:
   print (pcgreen + "I'm sorry, you lost. Computers will take over the world!")
print("Thank you for playing.\nGoodbye." + pcend)