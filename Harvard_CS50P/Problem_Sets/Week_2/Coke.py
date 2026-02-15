amount = 50

while amount > 0:
    print(f"Amount due: {amount}")
    coin = int(input("Insert coin: "))

    if coin in [5, 10, 25, 50, 75, 100]:
        amount -= coin

    else:
        print("Invalid input. Please try again.")
        print("*" * 20)

print(f"Change Owed: {abs(amount)}")

# amount_due = 50
#
# # Keep going as long as the person still owes money
# while amount_due > 0:
#     print(f"Amount Due: {amount_due}")
#     coin = int(input("Insert Coin: "))
#
#     # Check if the coin is one the machine actually accepts
#     if coin in [25, 10, 5]:
#         # Subtract the coin from the total owed
#         amount_due -= coin
#
# # Once the loop ends, they've paid enough!
# # (Note: If they paid extra, CS50 wants you to print the "Change Owed")
# print(f"Change Owed: {abs(amount_due)}")