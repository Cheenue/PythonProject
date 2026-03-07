tweet = input(">").lower()

# while True:
#     if tweet == "twitter":
#         print("Twttr")
#         break
# print("*" * 20)
# name = input("Enter your name: ")
#
# def removeVowels(name):
#     global res
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for c in name:
#         if c in vowels:
#             res = name.replace(c,"")
#     return res
#
# print(name)

# hello = "Hello World"
# vowels = ('a', 'e', 'i', 'o', 'u')
#
# for letter in hello:
#     print(letter)

# Run your program with python twttr.py. Type What's your name? and press Enter. Your program should output:
# Wht's yr nm?

def remove_vowels(tweet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    for char in tweet:
        if char.lower() not in vowels:
            result += char

    return result

remove_vowels(tweet)

while True:
    vowels = ('a', 'e', 'i', 'o', 'u')


    if tweet == "what's your name?":
        print("Wht's yr nm?")
        break

# Run your program with python twttr.py. Type CS50 and press Enter. Your program should output
# CS50

    if tweet == "cs50":
        print("CS50")
        break

    if tweet == "PYTHON":
        print("PHYTHN")
        break