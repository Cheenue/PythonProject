# Run your program with python fuel.py. Type 3/4 and press Enter. Your program should output:
# 75%
#
# response = input("> ")
# print("75%")

def get_percent():
    while True:
        try:
            # 1. Get input
            per = input("Fraction: ")

            # 2. Split the string into a list: ["3", "4"]
            x, y = per.split("/")

            # 3. Convert those parts to integers so we can do math
            numerator = int(x)
            # x is 3 BUT we are assigning it to an object
            denominator = int(y)
            # y is 4 BUT we are assigning it to an object

            # 4. Do the division
            fraction = numerator / denominator
            if numerator > denominator or numerator < 0:
                continue
            # this does the MATH and DIVIDES 3 by 4 which is 0.75 which is ALSO a FLOAT

            # 5. Return the result
            return fraction * 100
        #         this is 0.75 times 100 which EQUALS 75
        #             this is then RETURNED or STORED to get_percent()

        except (ValueError, ZeroDivisionError):
            # If the user types "cat" or "3/0", ask again
            pass

result = get_percent()
# this takes in what was returned in get_percent()
#     in this case it would be 75
rounded_result = round(result)
if rounded_result <= 1:
    print("E")
elif rounded_result >= 99:
    print("F")
else:
    print(f"{rounded_result}%")
# this ROUNDS 75 to the nearest whole number and then adds a PERCENT symbol into the string

# Run your program with python fuel.py. Type 1/4 and press Enter. Your program should output:
# 25%


# Run your program with python fuel.py. Type 4/4 and press Enter. Your program should output:
# F



# Run your program with python fuel.py. Type 0/4 and press Enter. Your program should output:
# E



# Run your program with python fuel.py. Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.



# Run your program with python fuel.py. Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.



# Run your program with python fuel.py. Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.



# Run your program with python fuel.py. Type -3/4 and press Enter. Your program should handle a ValueError and prompt the user again.



# Run your program with python fuel.py. Type 5/4 and press Enter. Your program should prompt the user again.



