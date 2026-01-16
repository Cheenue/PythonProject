unit = input("What unit are you using?")
temp = int(input("What temperature is the water?"))

# f - 212
# c - 100
# k - 373

if unit == "f":
    if temp == 212:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING!")
elif unit == "c":
    if temp == 100:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING!")
elif unit == "k":
    if temp == 373:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING!")
else:
    print("I don't know those unit!")