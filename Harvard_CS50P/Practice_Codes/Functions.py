intro = input("What is your name? ").strip().title()

# Split the user's name into first and last name
first, last = intro.split(" ")
# so why did i say first, last?
# how does python KNOW to split the answer from INTRO?
#     Python is SPLITTING whenever it sees a SPACE or " "
# What if i only wrote one word?
#   This would lead to a VALUE ERROR because PRINT was expecting 2 objects NOT 1

# print(f"Hello, {first}.")
# greeting()
#   this greeting DOESN'T exist yet to PYTHON because PYTHON is a TOP DOWN reader
def greeting():
    print(f"Hello, {first}.")

greeting()
print("*" * 50)

def hello(to):
    print("Hello,", to)

name = input("What is your name? ")
hello(name)
# when the FUNCTION is CALLED as in HELLO(NAME)
#     it TREATS NAME as if it was TO