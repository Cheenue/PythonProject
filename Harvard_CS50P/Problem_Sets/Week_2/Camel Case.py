#
# while True:
#     case = input("camelCase: ")
#
#     if case == "name":
#         print(f"snake_case: {case}")
#
#     elif case == "preferredFirstName":
#         replace = case.split()
#         print(f"{replace}")

# 1. Get the input (Don't lowercase it yet!)
camel = input("camelCase: ")

# 2. Prepare an empty string to hold the snake_case version
snake = ""

# 3. Loop through every character in the string
for char in camel:
    # 4. Check if the character is uppercase
    if char.isupper():
        # Add an underscore and the lowercase version of the letter
        snake += "_" + char.lower()
    else:
        # Otherwise, just add the letter as it is
        snake += char

# 5. Print the final result
print(f"snake_case: {snake}")