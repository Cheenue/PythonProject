# greeting = input("Type here: ").lower().strip()
#
# match greeting:
#     case "hello":
#         print("0")
#     case "how are you doing?":
#         print("$20")
#     case "what's happening?":
#         print("$100")
#
# print("*" * 50)

# Probably a better version than the one i have up there:

bank = input("Greeting: ").lower().strip()

if bank.startswith("hello"):
    print("$0")
elif bank.startswith("h") and not "hello" in bank:
    print("$20")
else:
    print("$100")