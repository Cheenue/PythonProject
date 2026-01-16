#What is your age?

# age = input("What is your age? ")
# happy = input("Are you happy as " + age + "? ")
# young_old = input("Would you rather be younger or older? ")
# reason_to_be = input("Why do you want to be " + young_old + "? ")
# perfect_age = input("What age would you like to be? ")

age = input('Enter your age: ')
days = float(age) * 365
guess = input("How many days do you think that is? ")
if int(guess) > days - 500 and int(guess) < days + 500:
    print("Whoa, you're really close!")
elif int(guess) < days:
    print(f'You guessed {guess} which is too low!')
elif int(guess) > days:
    print(f'You guessed {guess} which is too high!')
else:
    print(f'You\'re really off by a lot!')
print(f'Actually, you\'ve been alive for {days} days! You oldster!')

