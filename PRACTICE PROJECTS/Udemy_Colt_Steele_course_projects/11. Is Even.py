# def is_even(num):
#     if num % 2 == 0:
#         return True
#     # else:
#     #     you DON'T need else here
#     return False
# #       you can just leave it as a return and it'll do the same thing
#
# print(is_even(5))

# ***********************************************************************************

# we can simplify it further
# user_response = int(input("Enter a number: "))
#
# def is_even(num):
#     return num % 2 == 0
# # this will return IF IT IS TRUE and if it isn't then it will return FALSE
#
# print(is_even(user_response))

# ***********************************************************************************

# def slugify(phrase):
#     return phrase.lower().strip().replace(' ', '-')
#
# print(slugify("Hello my name i s Cheenue"))

# ***********************************************************************************

def count_vowels(word):
    count = 0
    # I have to create a COUNT because each character in the word is a number place
    for char in word:
        # char is just a word we chose for each SPOT in WORD
        if char in 'aeiou':
            # this is saying if the char from the FOR loop is a vowel in AEIOU then we'll add 1 to the counter?
            count += 1
    # if the FOR loop DOESN'T find a vowel then it starts over for the next character? but how does python know to MOVE ONTO THE NEXT CHARACTER?
    return count

print(count_vowels('banana'))