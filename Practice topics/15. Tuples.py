# Tuples
# You can't change the values of TUPLES after they exist meaning that they are IMMUTABLE!

# Example #1
dishes = ("burrito", "taco", "fajita", "quesadilla")

# Example #2
# single_tuple = ("First")
#     This DOES NOT work
# single_tuple = ("First",)
#     This works and is a TUPLE
#     It NEEDS to be followed by a COMMA to be a TUPLE
#     By having the comma there, it TELLS Python that it's NOT an expression but a TUPLE
# single_tuple = "First",
#     This works and is a TUPLE
#     It NEEDS to be followed by a COMMA to be a TUPLE
#     By having the comma there, it TELLS Python that it's NOT an expression but a TUPLE

sample_colors = ("red", "green", "blue")
print(type(sample_colors))
# It shows that it IS a TUPLE
print(sample_colors[1])
# This prints green

# Example 3
stuff = (1, 2, [])
# Tuples can have LISTS in them
stuff[2].append('hello')
# Although I can't CHANGE a tuple, I can CHANGE the LIST in the TUPLE
print(stuff)