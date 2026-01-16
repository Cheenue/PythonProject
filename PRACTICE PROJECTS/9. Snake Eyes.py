import random

roll_1 = random.randint(1,6)
roll_2 = random.randint(1,6)
roll_count = 1

while roll_1 != 1 or roll_2 != 1:
    print(roll_1, roll_2)
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
#     so i wrote this again because now it's giving roll_1 and roll_2 a new number to go through the while loop
    roll_count += 1

print(roll_1, roll_2)
print("Yay! SNAKE EYES!")
print(f'It took {roll_count} times to have both rolls be the same number.')

