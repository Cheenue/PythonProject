# replace(old, new[, count]

# cart = 'apples, oranges, eggs'
#
# print (cart)
#
# cart = cart.replace('apples', 'bananas')
# # I had to make the REPLACE method set to a variable CART so that then I printed it out, it wasn't the ORIGINAL string
# # Strings are IMMUTABLE meaning they can't change. So I had to set the ORIGINAL variable equal to a new STRING to then be able to print out the REPLACE changes.
#
# print(cart)


cart = 'apples, oranges, eggs'

# print (cart)
#
# cart = cart.replace('s', 'd', 2)
# # the count section told Python: "Find the first two 's' characters and swap them, then stop."
#
# print(cart)
# # output =
# # apples, oranges, eggs
# # appled, oranged, eggs



# find(sub[, start[, end]])¶
cart_of_s = cart.find('s', 1, 15)
print(cart_of_s)
# this will find the FIRST s in the variable CART
# but i can have a start and end as well which will find the index of the first s' AFTER the start index
