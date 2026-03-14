# print("hello, world)
#           ^
# SyntaxError: unterminated string literal (detected at line 1)
    # SyntaxError MEANS that SOMETHING IS WRONG WITH MY CODE

x = int(input("What is x? "))
# what if i put a STRING like the word CAT?
print(f"x is {x}")
# If I put CAT in it then i get a ValueError
#   ValueError: invalid literal for int() with base 10: 'CAT'

print("*" * 25)

#So now we have to use the TRY method to TEST things that could "break" the code and give us an error
try:
    y = int(input("What is y? "))
    # what if i put a STRING like the word CAT again?
    print(f"y is {y}")
except ValueError:
    print("y is not an integer")

print("*" * 25)

# what if i put the print("x is not an integer" OUTSIDE the Try/Except block?
try:
    z = int(input("What is z? "))
    # what if i put a STRING like the word CAT again?
except ValueError:
    print("z is not an integer")

print(f"z is {z}")

print("*" * 25)

# ELSE within the try/except block
try:
    xx = int(input("What is xx? "))
    # what if i put a STRING like the word CAT again?
except ValueError:
    print("xx is not an integer")
else:
    print(f"xx is {xx}")

# result: What is xx? cat
#         xx is not an integer

print("*" * 25)

# Let's LOOP this so that the code doesn't just STOP after we ask once

while True:
    try:
        yy = int(input("What is yy? "))
        # what if i put a STRING like the word CAT again?
    except ValueError:
        print("yy is not an integer")
    else:
        break
print(f"yy is {yy}")

print("*" * 25)

# Let's create a function with this and execute it

def main():
    zz = get_int()
    print(f"x is {zz}")

def get_int():
    while True:
        try:
            return int(input("What's zz? "))
            #   i changed the code so I'm not ASSIGNING ZZ to something I'm simply RETURNING it
            # return zz
            #     I COULD put the RETURN here but I could simplify it more
        except ValueError:
            # print("zz is not an integer")
        #   What if it's TOO noisy and I don't want to KEEP telling the USER that zz is NOT an integer?
        #       Well I can put the word PASS here and it will keep asking the user without prompting them that something is wrong inherently
            pass
        # else:
        #     return zz
#         I could just get RID of the ELSE and RETURN ZZ here
#     return zz
#         I'm putting an extra line here but how about I just MOVE the return to the ELSE indentation?

main()

print("*" * 25)
