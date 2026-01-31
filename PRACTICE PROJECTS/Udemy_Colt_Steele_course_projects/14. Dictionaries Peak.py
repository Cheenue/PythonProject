# The exercise uses the following "peak" dictionary:
peak = {
    "name": "Castle Peak",
    "height": 14264,
    "summit_log": [],
    "cell_reception": {
        "AT&T": "no reception",
        "T-Mobile": "poor"
    }
}
# Without touching the original variable declaration (above)...
# Add a "range" key to peak and set it equal to "Elk Mountains"
peak["range"] = "Elk Mountains"

# Add a "first_climbed" key to peak and set it equal to 1873

peak["first_climbed"] = 1873

# Whoops, there's a mistake with the peak "height".  Update it to 14265

peak.update({"height": 14265})
# this is right if I wanted to update a lot of items however I could just write it as: peak["height"] = 14265

# Add a "Verizon" to the "cell_reception" dict and set it equal to "good"

peak["cell_reception"]["Verizon"] = "good"
# this is selecting cell_reception within the PEAK dictionary and then ADDING "VERIZON" to is correct?
# so what i did was ACCESS "cell_reception" dictionary and then I ADDED "verizon"

# You just summited the peak! Add your name to the "summit_log" list

peak["summit_log"].append("Cheenue Thao")

# Let's rename "height" to "elevation":
# Remove "height" from the dict and store the result in a variable.

old_height = peak.pop("height")
# this REMOVED it from PEAK and assigned it to a new variable

# Use the value for "height" and store it in the dict under they key "elevation"

peak["elevation"] = old_height

# # .append is ONLY for lists
# # this is saying that for the new value of elevation, i will put in the value in "height"
#     # Brackets on the left of the = mean: "This is where I want to save the data."
#     # Brackets on the right of the = mean: "This is where I am getting the data from."
#
# # Loop over the values in the dictionary and print them all out.  Don't ask why, just do it :)
#

for value in peak.values():
    print(value)


# Loop over the keys AND values in the dictionary and print them all out in the following format:
# key -> value
# (print an arrow between each pair)

for key, value in peak.items():
    print(f'{key} -> {value}')


# A huge earthquake/meteor/forestfire/tsunami has destroyed the peak.  Please empty out the entire dictionary.

peak.clear()
print(peak)


