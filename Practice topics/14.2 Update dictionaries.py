d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4}

d1.update(d2)
# this COMBINED d1 and d2

print(d1)
# d1 is UPDATED now with d2 added onto it
print(d2)
# But we can see that d2 didn't change any values in it

# Another way to combine the two is below but this is the OLD way
d3 = {**d1, **d2}
print(d3)

# From python 3.9 and newer, we will use this method
d4 = d1 | d2
print(d4)

# We can have NESTED dictionaries too!