# for i in [0, 1, 2]:
#     print(i)
#
# print("*" * 50)
#
# for x in range(4):
#     print(x)
#
# print("*" * 50)
#
# for i in range(3):
#     print("meow")
# # Notice how we don't even USE i in this code BUT we can write it like this because it is MORE PYTHONIC
# for _ in range(3):
#     print("bark")
#
# print("*" * 50)
#
def main():
    number = get_number()
    meow (number)
#
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n
#
# def meow(n):
#     for _ in range(n):
#         print("meow")
#
# main()
#
# print("*" * 50)
#
# students = ["harry", "hermoine", "ron"]
# houses = {"Hermoine": "Gryffindor",
#           "Harry": "Gryffindor",
#           "Ron": "Gryffindor",
#           "Draco": "Slytherin"
#           }
#
# print(houses["Hermoine"])
# print(houses["Harry"])
# print(houses["Ron"])
# print(houses["Draco"])
#
# print("*" * 50)
#
# for student in houses:
#     print(student)
# # when we iterate over a DICTIONARY it prints out ONLY the KEYS!
# print("*" * 50)
# for student in houses:
#     print(student, houses[student], sep=", ")
# #     so the sep= function separates the KEY and VALUE in the DICTIONARY and we set it to PLACE a ", " between them
#
# #
# # # basic way of printing out EVERYONE in the LIST
# # print(students[0])
# # print(students[1])
# # print(students[2])
# #
# # # pro way of printing out everyone with a loop
# #
# # for student in students:
# #     print(student)
# #
# # for kid in len(students):
# #     # this is wrong because len() RETURNS a number not a RANGE
# #     print(kid)
#
# # correct way of doing this
# for person in range(len(students)):
#     # print(students[0])
#     print(person + 1, students[person])
# print("*" * 50)

hogwarts = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]

for student in hogwarts:
    print(student["name"], student["house"], student["patronus"], sep=", ")

print("*" * 50)

def print_square(size):
    # For each row in the square
    for i in range(size):
        # For each brick in the row
        for j in range(size):
            # Print brick
            print("<>", end="")
        # Move to the next line after finishing a row
        print()

def main():
    print_square(3)

main()