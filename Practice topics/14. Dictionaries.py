# empty_dictionary = {}
#
# movie = {"title": "Amadeus", "imdb_score": 8.3}
# # KEY is the left and VALUE is the RIGHT of the ":"
#
# print(movie)
# # this prints out {'title': 'Amadeus', 'imdb_score': 8.3}
# print(movie["title"])
# # this SELECTS the KEY "title" from movie and outputs Amadeus
# movie["title"] = "AMADEUS"
# # this CHANGES the data in the dictionary so the title now is UPPERCASE
# print(movie)
#
# movie["imdb_score"] += 3.0
# print(movie)
# # this changed the data in the dictionary by ADDING to the score
#
# movie['is_great'] = 50
# # this ADDS a new key to the dictionary and I can make it pair up with anything BUT LISTS or DICTIONARIES
# print(movie)
#
# # KEYS have to be UNIQUE in a dictionary but VALUES can be the same in it

grocery_prices = {
    "milk": 3.99,
    "eggs": 4.50,
    "bread": 2.25,
    "apples": 0.75,
    "bananas": 0.75,  # Notice: Different keys, same value!
    "cheese": 5.00
}

# print("milk" in grocery_prices)
# IN operator only looking at KEYS

# USING GET()
product = input("What product are you buying today? ")
# price = grocery_prices.get(product)
# if(price):
#     print(f"The price of {product} is ${price} dollars")
# else:
#     print("Sorry, that product is not available")

# USING POP(), CLEAR(), DEL()
pop = grocery_prices.pop(product)
print(pop)
# this will RETURN the VALUE of the KEY that I chose in the parenthesis