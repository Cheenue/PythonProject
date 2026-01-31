# Sets
# Unordered collections with NO duplicate elements
# EVERY VALUE has to be UNIQUE
# ONLY IMMUTABLE elements in them so NO LISTS OR DICTIONARY
# THEY ARE UNORDERED!

# Example #1
evens = {2, 4, 6, 8}
print(type(evens))
# This is a SET
# it uses CURLY brackets

more_evens = {2, 4, 12, 24, 2, 4}
print(more_evens)
# This OUTPUTS {24, 2, 4, 12}
# So it DOESN'T REPEAT NUMBERS

empty_set1 = set()
# THIS is an EMPTY SET
empty_set2 = {}
# This is a DICTIONARY

# ADD()

even = {2, 4, 6, 8}
even.add(12)
print(even)
# THis prints {2, 4, 12, 6, 8}

# REMOVE()
even.add(5)
# ADDS 5
print(even)
even.remove(5)
# Then I REMOVE 5 from the set
print(even)
# even.remove(7)
#   this will give me an ERROR

# DISCARD()
even.discard(9)
# 9 DOESN'T EXIST in even
# This DIDN'T give me an ERROR!
print(even)
