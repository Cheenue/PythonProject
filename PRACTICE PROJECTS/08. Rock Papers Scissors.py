# I’d like for you to build a very simple implementation of the game Rock Paper Scissors.  If you’re unfamiliar with the game, here’s how it works... Two players each pick their move: rock, paper, or scissors.  Each move beats one other move and loses to one other move:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
#
# Your implementation will be a one player game that has a computer “AI” that randomly picks a move.
#
# See the game in action below (user input in green):
#

player_one = input("What are you going to throw out? ").lower()
player_two = input("What are you going to throw out? ").lower()

if player_one == "rock":
    hands_one = 1
elif player_one == "paper":
    hands_one = 2
elif player_one == "scissors":
    hands_one = 3
else:
    hands_one = 0
# 0 acts as NULL meaning that if player_one puts something else as an input like dragon or lizard that is seen to Python as NULL or EMPTY


if player_two == "rock":
    hands_two = 1
elif player_two == "paper":
    hands_two = 2
elif player_two == "scissors":
    hands_two = 3
else:
    hands_two = 0
# 0 acts as NULL meaning that if player_one puts something else as an input like dragon or lizard that is seen to Python as NULL or EMPTY

if hands_one > 0 and hands_two > 0:
    if hands_one == hands_two:
        print("It's a draw!")
    elif hands_one == 1 and hands_two == 3:
        print("Player one wins!")
    elif hands_one == 3 and hands_two == 1:
        print("Player two wins!")
    elif hands_one > hands_two:
        print("Player one wins!")
    else:
        print("Player two wins!")
else:
    print("NOBODY WINS!")



# if rock == hands_one
#
# print(rock)