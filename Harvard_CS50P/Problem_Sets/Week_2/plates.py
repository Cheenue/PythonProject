# Run your program with python plates.py. Type CS50 and press Enter. Your program should output:
# Valid

# while True:
#     if response == "CS50":
#         print("Valid")
#         break
#
#     else:
#         print("Invalid")
#         break

response = input(">")

def is_valid(response):
    if not 2 < len(response) < 6:
        # i originally had if len(response) > 2 and len(response) < 6 BUT the IDE wanted to simplify it to that
        return False
    if not response[0:2].isalpha():
        return False

    if not response.isalnum():
        return False

    return True

if is_valid(response):
    print("Valid")
else:
    print("Invalid")

# Run your program with python plates.py. Type CS05 and press Enter. Your program should output:
# Invalid

# Run your program with python plates.py. Type CS50P and press Enter. Your program should output
# Invalid

# Run your program with python plates.py. Type PI3.14 and press Enter. Your program should output
# Invalid

# Run your program with python plates.py. Type H and press Enter. Your program should output
# Invalid

# Run your program with python plates.py. Type OUTATIME and press Enter. Your program should output
# Invalid