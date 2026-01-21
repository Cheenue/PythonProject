# nested_list = [1.2, 3, 4, [8, 6]]
# print(nested_list[1])
# # this prints out 3
# print(nested_list[3][0])
# # this prints out 8
#
# couples = [
#     ["Beyonce", "Jay-Z"],
#     ["Johnny", "June"],
#     ["John", "Yoko"],
#     ["Will", "Jada"]
# ]
#
# for couple in couples:
#     # this is selecting which NESTED LIST in the LIST COUPLES
#     for person in couple:
#         # this is selecting with object in the NESTED LIST
#         print(f"Sending invite to...{person}")
#
# sample_list = [1, 2, 3] + [4, 5, 6]
# print(sample_list)
# # this will combine both of those lists into one
#
# flavors = ["apple", "banana", "cherry"]
#
# response = input("What flavors would you like? ")
#
# while response.lower() not in flavors:
#     response = input("Please pick one of our options! Try again: ")
#
# print(f'Okay, {response} ice cream coming right up!')

# ******************************************************************

# count()
# langs = ["Python", "Java", "C++"]
# print(langs.count("Python"))
# # count() has to be the EXACT value in the list to show up instead of 0
#
# # ******************************************************************
#
# # split()
# invited = ["Paul...Cheng...Cheenue".split(".")]
# print(invited)
# # this printed out [['Paul', '', '', 'Cheng', '', '', 'Cheenue']]
# invitees = ["Paul...Cheng...Cheenue".split("...")]
# print(invitees)
# # this printed out [['Paul', 'Cheng', 'Cheenue']

# ******************************************************************

# join()
# this is STRICTLY a STRING method
# letters = ["a","b","c","d","e","f","g"]
# print("*".join(letters))
# # this prints out a*b*c*d*e*f*g
# # so * is INSERTED between each string in the list container
#
# numbers = ["0","1","2","3","4","5","6"]
# print("#.".join(numbers))
#
# numbre = [1, 2, 3, 4, 5, 6, 7, 8]
# print("!".join(numbre))
# the error I got was this: TypeError: sequence item 0: expected str instance, int found
# Reason why is that I can't JOIN different types of data together

# ******************************************************************

# list unpacking
race_results = ["bill", "ted", "jimothy", "dan", "tom", "Erica"]
# gold, silver, bronze = race_results
# Error I got was ValueError: too many values to unpack (expected 3, got 6)
# what we can do is put an * before a variable and it will contain ALL the remaining values after it
gold, silver, bronze, *losers = race_results
print(silver)
# this will print out TED because it follows how we assigned the variables

# ******************************************************************

r1 = [1, 2, 3]
r2 = r1.copy()

print(r1 == r2) # True (Content is the same)
print(r1 is r2) # False (IDs are different)
# ID's are like the SSN of each variable. No variable ID is the same
# for example i would write it like this print(id(r1)) and this would show a different one than if i wrote it for r2