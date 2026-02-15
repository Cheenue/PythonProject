from os.path import sep


# def main(_):
#     get_numbers()
#     add(get_numbers, second_number())
#
# def add(x, y):
#     addition = x + y
#     print(addition)
#
# def get_numbers():
#     while True:
#         number = input("Enter the first number to add: ")
#         commas = number.replace("", " ")
#         actual_number = int(commas)
#         return actual_number


while True:
    n1 = (input("Enter a number: "))
    try:
        n11 = float(n1)
        print(n11)
        break
    except:
        print("Please enter a number")

while True:
    n2 = (input("Enter another number: "))
    try:
        n22 = float(n2)
        print(n22)
        break
    except:
        print("Please enter a number")
print("*" * 20)
print(n1.__add__(n2))
# #
# def add(n1, n2):
#     return n1 + n2
# print(add(n1, n2))