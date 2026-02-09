#
# print("\U0001F642")
#
# print("\N{slightly smiling face}")

# input = input("Type here: ")
#
# print(f'{input} \U0001F642')

# if input == "hello :)":
#     print(f'{input} \U0001F642')
# elif input == "goodbye :(":
#     print(f'{input} \U0001F61F')

input = input()

new_input = input.replace(":)", "\U0001F642").replace(":(", "\U0001F641")

print(new_input)