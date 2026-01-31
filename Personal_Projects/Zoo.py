import self

zoo_staff = 0
zoo_total_animals = 0
zoo_storage = []


# while True:
#     first_question = input("Do you want to work at the zoo? ").lower()
#     if first_question == "yes":
#         zoo_staff += 1
#         print(f"Zoo staff is currently at {zoo_staff}")
#     elif first_question == "no":
#         print("Have a good day. The pleasure was all mine")
#         break
#     else:
#         print("Try again another time.")
#         break
# print(zoo_staff)
#
# I first wanted to create the staff but then went against it since this is a zoo I'm creating. I wanted to use the CRUD method to Creat/Add, Read, Update, and then be able to Delete in the same code

class Animal:
    def __init__(self, type, name, height, weight, power):
        self.type = type
        self.name = name
        self.height = height
        self.weight = weight
        self.power = power

    def __repr__(self):
        return f"{self.name.capitalize()} the {self.type}"
# while True:
#     choice = first_question = input("Add an animal to the zoo? ").lower()
#     if choice == "yes":
#         # Now we have to collect the data about the animal
#         t = input("What type of animal is it? ").lower()
#         n = input("What name is it? ").lower()
#         h = input("What is its height in centimeters? ").lower()
#         w = input("What is its weight in kilograms? ").lower()
#         p = input("What is its power level (0-100)? ").lower()
#
#         new_animal = Animal(t, n, h, w, p)
#
#         zoo_storage.append(new_animal)
#
#         print(f"Zoo storage is currently at {zoo_storage}")
#     elif choice == "no":
#         print("The zoo doesn't like your animal anyways.")
#     else:
#         print("Try again another time.")
#         break

while True:
    action = input("What would you like to do? (CREATE, READ, UPDATE, or DELETE) ").lower()

    # CREATE/ADD a new animal
    if action == "create":
        t = input("What type of animal is it? ").lower()
        n = input("What name is it? ").lower()
        h = input("What is its height in centimeters? ").lower()
        w = input("What is its weight in kilograms? ").lower()
        p = input("What is its power level (0-100)? ").lower()

        new_animal = Animal(t, n, h, w, p)

        zoo_storage.append(new_animal)

        print(f"Zoo storage is currently at {zoo_storage}")

    elif action == "read":
        print("Zoo inhabitants")
        print("*"*25)
        for animal in zoo_storage:
            print(animal)
        print(f'Total number of animals in the zoo: {len(zoo_storage)}')

    elif action == "update":
        name_to_find = input("What name would you like to update? ").lower()
        for animal in zoo_storage:
            if animal.name == name_to_find:
                new_name = input("Enter new name. ")
                animal.name = new_name
                print(f"Update was successful. New name: {new_name}")

    elif action == "delete":
        remove_animal = input("What animal would you like to delete? ").lower()
        for animal in zoo_storage:
            if animal.name == remove_animal:
               zoo_storage.remove(animal)

    elif action == "q":
        break

    else:
        print("Invalid command. Try again.")

