# Restaurant check PRACTICE

# list different types of food with prices
# the items will have to be a FLOAT
# orange = "$6.50"
# spinach = "$3.25"
#
# orange_price = float(orange.replace("$"," "))
# spinach_price = float(spinach.replace("$"," "))

# vegetable = input("Which vegetables did you have? ")


# add the total bought to consume

total = float(input("What is your total today? "))

# Leaving a tip means converting the percentage to a FLOAT and then MULTIPLYING it with the total

tip_1 = input("How much do you want to tip in %? ")
tip_2 = float(tip_1.replace("%",""))

tip_total = tip_2 / 100
tip_ttl = total * tip_total
total_price = total + tip_ttl

# total = partial total * (tip / 100)

# write the NEW total

print(total_price)