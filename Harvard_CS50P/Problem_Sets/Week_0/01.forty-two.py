number = input("Type here: ").lower().strip()

# I could write it this way but this is clunky
# strip() was needed for this
if number == "42":
    print("Yes")
elif number == "Forty Two":
    print("Yes")
elif number == "forty-two":
    print("Yes")
else:
    print("no")
#     problem with this is that if i put an extra SPACE before or after the input, it would automatically output NO

# This is the professional way
match number:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")