grocery_list = []
removed_list = []
completed_list = []
original_list = []

while True:
    task = input("What would you like to add to your grocery list? ")


    if task == "q":
        break

    elif task.isnumeric():
        num = int(task) - 1
        choice = input("Type 'b' for bought and type 'r' if item is to be removed: ")
        if choice == "b":
            item = grocery_list.pop(num)
            completed_list.append(item)
        elif choice == "r":
            item = grocery_list.pop(num)
            removed_list.append(item)
        else:
            print("Sorry, that's not a valid choice. Choose from 'b' for bought and 'r' for removed.")

    # elif task.isnumeric():
    #     num = int(task)-1
    #     removed_item = grocery_list.pop(num)
    #     removed_list.append(removed_item)
    #     print(f'Removed {removed_item} from your grocery list')
    # I removed this because I wanted to show to the person that people make multiple lists and it's not just a buy or remove system.

    else:
        grocery_list.append(task)
        original_list.append(task)

    print("Current grocery list:")

    count = 1
    for product in grocery_list:
        print(f'{count}. {product}')
        count += 1

print("Original grocery list:")
orilist = 1
for product in original_list:
    print(f'{orilist}. {product}')
    orilist += 1

print("Items bought:")
idx = 1
for pdone in completed_list:
    print(f'{idx}. {pdone}')
    idx += 1

print("Items removed:")
remove = 1
for waste in removed_list:
    print(f'{remove}. {waste}')
    remove += 1

# DESIGN RATIONALE & DEVELOPMENT JOURNEY:
# This program was developed using an iterative approach to solve real-world list management needs.
# 1. Initial Phase: Established basic list storage and display functionality.
# 2. Evolutionary Phase: Identified the need for state-based categorization (Bought vs. Removed)
#    to distinguish between successful task completion and intentional omission.
# 3. Persistence Phase: Implemented 'original_list' to maintain data integrity, allowing for
#    a historical "audit trail" that remains unaffected by the destructive .pop() operations
#    used in the active 'grocery_list'.
#
# Final Result: A comprehensive tracking system that provides the user with a 360-degree view
# of their planning, active progress, and final outcomes.