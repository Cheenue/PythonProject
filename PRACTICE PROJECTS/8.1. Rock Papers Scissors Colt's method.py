from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move

comp_num = randint(1,3)

# Ask a user to enter their move

player_move = randint(1,3)
compai_move = randint(1,3)

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move

if player_move == 1:
    print(rock)
if player_move == 2:
    print(scissors)
if player_move == 3:
    print(paper)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move

if compai_move == 1:
    print(rock)
if compai_move == 2:
    print(scissors)
if compai_move == 3:
    print(paper)

# Figure out who wins and print the result!

if player_move == compai_move:
    print("It's a draw!")
elif player_move == 1 and compai_move == 2:
    print("You win!")
elif player_move == 2 and compai_move == 3:
    print("You win!")
elif player_move == 3 and compai_move == 1:
    print("You win!")
else:
    print("AI wins!")