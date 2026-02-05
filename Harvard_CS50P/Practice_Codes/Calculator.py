# x = 1
# y = 2
#
# z = x + y
#
# print(z)
# print("*" * 50)
#
# # interactive now
#
# x = int(input("what is x? "))
# y = int(input("what is y? "))
# z = x + y
# print(z)
# print("*" * 50)
#
# # rounding with FLOATS
#
# # round(number, ndigits)
#
# # difference between the two
#     # round(z, 2) → gives you 10.5 (It drops the extra zero).
#     # f"{z:.2f}" → gives you 10.50 (It keeps the "padding").
#
# x = float(input("what is x? "))
# y = float(input("what is y? "))
#
# z = round(x + y)
#
# print(z)

def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))

def square(x):
    return x ** x

main()