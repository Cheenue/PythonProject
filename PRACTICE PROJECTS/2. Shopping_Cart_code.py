# Write a Python script that does the following:
#
# - Prints out a “banner” to welcome users to our shop
# - Asks the user for the name of the item they are buying
# - Asks the user for the price of that item
# - Asks the user for the quantity they are purchasing
# - Prints out a message that includes their subtotal (quantity 𝚡 price)

print("WELCOME TO OUR STUPID SHOPPING CART! \n ****************************************")
product = input("What item are you looking to buy? ")
cost = float(input("How much does it cost? "))
# Changed it to a float because the cost of items go to a 2 place decimal which an INT cannot do
how_many = int(input("How many are you planning to buy today? "))
# I kept this as an INT because this is on quantity
print(f'Added {how_many} {product} to your shopping cart \nYour subtotal comes out to be ${cost * how_many:.2f}. ')
# I used the f' function to add in variables used earlier in my code without it being a STRING.
# Then I used :2f to indicate that i wanated the decimal to go to 2 places
