#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

for letter in word:
    print(letter)

print("*" * 25)

# Write a while loop that does the same thing!

index = 0
while index < len(word):
    print(word[index])
    index += 1

print("*" * 25)

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

num = 100
while num < 141:
    print(num)
    num +=2

print("*" * 25)

# Write a for loop that does the same thing (with range())

for even in range(100, 141, 2):
    print(even)

print("*" * 25)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

silly = input("Passphrase? ")

while not silly == "sillygoose":
    # IN WORDS I CAN UNDERSTAND: while the answer to SILLY is NOT "sillygoose" then we RUN this loop
    silly = input("Passphrase? ")
# because it is FINALLY silly goose, then the loop doesn't happen anymore

print("YAY")

# because the loop doesn't happen anymore THEN it can print out YAY
