from random import randint
# I have to import this if i'm using randint
num_dice = int(input("how many dice are you rolling? "))
num_sides = int(input("how many sides on each die? "))

while True:
    result ="*"
    for die in range(num_dice):
            # they use DIE but that's for each number in the range right
            # die variable is for EACH single number adding up to num_dice
            # num_dice is the COUNT of how many numbers it takes to go through the loop
        rand = randint(1,num_sides)
            # this is a variable RAND which is equal to RANDINT(1, num_sides) so it starts at 1 and ends at num_sides
            # it's only num_sides-1 for the RANGE function
        result += f"{rand}|"
    #      result += f"{rand}|" is saying RESULT 1 = X | RESULT 2 = Y | RESULT 3 = Z |
    #      because it's adding this onto the sentence for the full answer due to the loop until it reaches the count in the loop condition
    print(result)
            # this also prints out the FIRSt result and then the RESULT in the loop afterwards
    #         in the end it prints whatever rand is from the for loop so this could be the cumulative sentence that it has been writing due to the loop
    reply = input("Roll again? (q to quit)")
            # then it asks this question again which will go through the loop again until i press q?
    if reply == "q":
        break
    #         this stops the loop
