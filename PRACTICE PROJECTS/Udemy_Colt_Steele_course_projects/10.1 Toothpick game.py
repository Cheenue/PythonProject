# from random import randint
# Implement a version of the “classic” matchsticks/toothpicks two player game.  We start with 13 toothpicks, and plays take turns removing 1, 2, or 3 toothpicks at a time.  The person who removes the last toothpick wins.

toothpick = 13
toothpicks = " | "
# toothpickss = int(toothpicks)
#   this doesn't work because toothpicks is a STRING ugh how do i do this
# print(toothpicks)

while toothpick > 0:
    print(toothpicks * toothpick)

    p1 = int(input("P1: How many do you want to take out? 1 or 2 toothpicks? "))
    toothpick -= p1
    # print(toothpick)

    if toothpick <= 0:
        print("P1 wins!")
        break

    print(toothpick * toothpicks)

    p2 = int(input("P2: How many do you want to take out? "))
    toothpick -= p2

    if toothpick <= 0:
        print("P2 took the last one! P2 WINS!")
        break

#  while toothpick < 14 and toothpick > -1:
#     player_one = int(input("How many toothpicks will you take out? (1) or (2) "))
#     player_two = int(input("How many toothpicks will you take out? (1) or (2) "))








    # for pick in range(1, 3):
        # print(toothpicks - pick)
        # # so toothpicks is a string so how do i subtract toothpicks in this game?
    #     if pick == player_one:
    #         # print(toothpick * player_one )
    # #     problem here is that it's NOT USING toothpicks of 13 but I want to take AWAY from TOOTHPICKS and then print it out
    #         print((toothpick - player_one) * toothpicks)
    #     elif pick == player_two:
            # print(toothpick * player_one )
             #     problem here is that it's NOT USING toothpicks of 13 but I want to take AWAY from TOOTHPICKS and then print it out
            # print((toothpick - player_two) * toothpicks)
        # player_one = int(input("How many toothpicks will you take out? (1) or (2) "))
        # player_two = int(input("How many toothpicks will you take out? (1) or (2) "))
        #     this doesn't work if i put the input here
        # if pick == player_one and pick > player_two:
        #     print((toothpick - player_one) * toothpicks)
        # elif pick == player_two and pick > player_one:
        #     print((toothpick - player_two) * toothpicks)
        # else:
        #     print((toothpick - player_one) * toothpicks)

    # toothpick -= pick

