# # Create a simple script that calculates a user’s body mass index.
# #
# # 1. Prompt a user to enter their height (in inches) and their weight (in pounds).
# # 2. Next, calculate their BMI using the formula: **(weight in pounds x 703) / (height in inches x height in inches)**
# # 3. Output a message including their BMI number and category according to the following table:
# #
# # > **< 16.0**    Severely Underweight
# # **16.0 - 18.4**   Underweight
# # **18.5 - 24.9**   Normal
# # **25.0 - 29.9**   Overweight
# # **30.0 - 34.9**   Moderately Obese
# # **35.0 - 39.9**   Severely Obese
# # **> 39.9**   Morbidly Obese
# # >
#
# print(f"Your BMI is {BMI}.")
# I wrote this code because I needed to see if I did the math right or not.

# if BMI < 16:
#     print(f"Your BMI is {BMI}. You are severely underweight.")
# elif BMI < 18 and BMI > 16:
#     print(f"Your BMI is {BMI}. You are underweight.")
# elif BMI < 24.9 and BMI > 18:
#     print(f"Your BMI is {BMI}. You are normal.")
# elif BMI < 29.9 and BMI > 25:
#     print(f"Your BMI is {BMI}. You are overweight.")
# elif BMI < 34.9 and BMI > 30:
#     print(f"Your BMI is {BMI}. You are moderately obese.")
# elif BMI < 39.9 and BMI > 35:
#     print(f"Your BMI is {BMI}. You are severely obese.")
# else:
#     print(f"Your BMI is {BMI}. You are morbidly obese.")
# THIS IS HOW I ORIGINALLY DID IT

# THIS IS HOW COLT STEELE DID IT!

# This is my final result

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
BMI = float((weight*703) / (height**2))
BMI = round(BMI, 2)

if BMI < 16:
    result = "severely underweight"
elif BMI < 18.5:
    result = "underweight"
elif BMI < 25:
    result = "normal"
elif BMI < 30:
    result = "overweight"
elif BMI < 35:
    result = "morbidly obese"
elif BMI < 40:
    result = "severely obese"
else:
    result = "BEYOND GONE!"

print(f'Your BMI is {BMI}. You are {result}.')