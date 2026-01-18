# scream()
# # this will NOT print out AHHHHHHHHH!!!! because it hasn't been defined yet
# # This needs to come AFTER I have defined it.
#
# def scream():
#     print("AHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!" * 5)
#
# scream()
# this recalls scream which i defined earlier and mentions it again

# ***********************************************************************************

# def laugh(intensity):
    # print("haha" * 20)
#     # this was how we USED to do it
#     print("haha" * intensity)
#     # We have to do it this way to make it not HARD CODED into the code
#
# laugh(1)
# laugh(4)
# laugh(10)

# that number in the function laugh() is the counter of how many time it will be multiplied in the function
# INTENSITY is just a placeholder or empty variable that WE will put in
# hold up, could we define intensity placeholder before as an INPUT and then that way laugh will dynamically change?

# ***********************************************************************************

def laugh(intensity):
    # so intensity here is the PLACEHOLDER
    # PLACEHOLDER can be called ANYTHING
    print("haha" * intensity)

# 1. Ask the user for the value
user_choice = int(input("How much do you want to laugh? "))

# 2. Pass that value into the function
laugh(user_choice)
# user_choice here is the ARGUMENT
# THE ARGUMENT is the INPUT when you RUN a FUNCTION