# modulo % operator

def main():
    x = int(input("What if x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
#     I could write it like this: return True if n % 2 == 0 else False
#       an even BETTER CLEANER way to write this is RETURN N % 2 == 0

main()

print("x" * 25)

name = input("What's your name? ")

# this is version 1
# which is good and how a beginner would write it out
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

print("x" * 25)

# this is version 2
# which is a little better but can be improved
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

print("x" * 25)

name = input("What's your name? ")

# this is version 3
# we are using the MATCH thing here which matches and then uses case for the specific name
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        # the _ is a catch all like ELSE
        print("Who?")

print("x" * 25)

# this is version 4
# which is a lot cleaner and simpler to read
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        # the "|" or PIPE is saying the equivalent of Harry or Hermoine or Ron
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        # the _ is a variable name that means "I don't care about this value"
        #   it also means, "It serves as a "throwaway" or "don't care"
        print("Who?")