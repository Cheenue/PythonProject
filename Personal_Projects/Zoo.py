import uuid
import time

zoo_staff = 0
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
# I first wanted to create the staff but then went against it since this is a zoo I'm creating. I wanted to use the CRUD method to Create/Add, Read, Update, and then be able to Delete in the same code

class Animal:
    def __init__(self, name, type, height, weight, power):
        self.id = str(uuid.uuid4())[:8]
            # Generates a short 8-character ID
            # uuid4() creates a random UUID
            # Universally Unique Identifier (UUID) version 4
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight
        self.power = power

    def __repr__(self):
        return f"{self.name.capitalize()} the {self.type.capitalize()}"
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
    action = input("\nWhat would you like to do? (CREATE, READ, UPDATE, DELETE or 'Q' to quit): ").lower()

    # CREATE/ADD a new animal
    if action == "create":
        n = input("What is its name? ").lower()
        t = input("What type of animal is it? ").lower()
        while True:
            h = input("What is its height in centimeters? ").lower()  # do not convert to int here
            try:
                v1 = int(h)
            except ValueError:
                print("That's not an integer.")
            else:
                break
        while True:
            w = input("What is its weight in kilograms? ").lower()
            try:
                v2 = int(w)
            except ValueError:
                print("That's not an integer.")
            else:
                break
        while True:
            p = input("What is its power level (0-100)? ").lower()
            try:
                v3 = int(p)
            except ValueError:
                print("That's not an integer.")
            else:
                break

        new_animal = Animal(n, t, h, w, p)

        zoo_storage.append(new_animal)

        power =  int(p)

        if power < 0 or power > 100:
            print("Error: Power level must be between 0 and 100!")
            continue
        else:
            print(f"Successfully added {n} to the zoo!")
            time.sleep(0.5)
            print(f"The Zoo currently has these animals: {zoo_storage}")


    elif action == "read":
        print("Zoo inhabitants")
        print("*"*25)
        for animal in zoo_storage:
            print(f"--- {animal.name.upper()} ---")
            print(f"Animal ID: {animal.id}")
            print(f"  🐾 Species: {animal.type.capitalize()}")
            print(f"  📏 Height:  {animal.height}cm")
            print(f"  ⚖️ Weight:  {animal.weight}kg")
            print(f"  ⚡  Power:   {animal.power}/100")
            print("-" * 25)

    elif action == "update":
        name_to_find = input("What name would you like to update? ").lower()
        for animal in zoo_storage:
            if animal.name == name_to_find:
                new_name = input("Enter new name. ")
                animal.name = new_name
                print(f"Update was successful. New name: {new_name}")

    elif action == "delete":
        remove_id = input("Enter the ID of the animal to remove: ").lower()
        # This is a "List Comprehension" - the professional way to filter lists
        original_count = len(zoo_storage)
        zoo_storage = [animals for animals in zoo_storage if animals.id != remove_id]

        if len(zoo_storage) < original_count:
            print(f"Success! Animal with ID {remove_id} has been removed.")
        else:
            print(f"Error: No animal found with ID {remove_id}.")

    elif action == "q":
        break

    else:
        print("Invalid command. Try again.")

if len(zoo_storage) == 1:
    print(f"The Zoo has {len(zoo_storage)} animal in total.")
elif len(zoo_storage) > 1:
    print(f"The Zoo has {len(zoo_storage)} animals in total.")