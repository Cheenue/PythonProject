first_name = len(input("Enter your first name: "))
last_name = len(input("Enter your last name: "))

if first_name > 7 and last_name > 7:
    print("Your first and last name is long enough")
# EDIT 4 [I TOOK OUT THIS LINE OF CODE] elif first_name < 7 and last_name < 7:
#     print("Your first and last name is too short.")
# EDIT 5: I had to take out this section because it interfered with my last elif statement
#     what happened is that if I put a name like colt steel, the code would hit this statement first and NEVER hit the last line of code which I wanted it to do in the first place
# EDIT 2: I was having an issue where ALL my answers were giving me this output so I had to take out the "=" sign and add an "and" operator so that BOTH sides had to be true for it to give this output.
# EDIT 3: I had the "OR" operator and it would show that my first name is 7 characters but not my last and defaulted it to give that output.
elif first_name >= 7 and last_name >= 7:
    print("You've got a pretty cool name!")
elif first_name <= 7 and last_name >= 7:
    print("You've got a pretty cool name doofus!")
elif first_name >= 7 and last_name <= 7:
    print("You've got a pretty cool name! NERD!")
elif first_name <= 7 and last_name <= 7:
    print("You've got an alright name")
else:
    print("Your first and last name is average.")

# EDIT 1: the issue with my first edit of code is if they have a short first name and long last name then the code will output that your first and last name is average
# My latest edit should fix this issue