# for outer in range (1, 5):
#     print(outer)
#     for inner in range(1, 6):
#         print("\t", inner)
#         the INNER loop has to run entirely before it can move onto the NEXT loop in OUTER (1-4)

# for die in range(1, 6):
#     print(die)
#     for roll in range(1, 6):
#         print("\t", roll)

# for sets in range(1, 4):
#     print(sets)
#     for reps in range(1, 11):
#         print("\t", reps)

for room in range(1, 4):
    for dirty in range(1):
        if room != 1:
            print("\t", f'You\'ve cleaned {room} rooms today')
        # this IF statement includes ROOM but it is needed for the ELSE statement and also so that IF ROOM is NOT 1 in the BIGGER Loop then it'll print out the above statement
        else:
            print(f'You\'ve cleaned {room} room today')
#             if ROOM is anything EXCEPT 1 which it will be 2 and 3, it will print out the above statement

for room in range(1, 4):
    if room != 1:
            print("\t", f'You\'ve cleaned {room} rooms today')
    #     it's printing this whenever room ISN"T 1 and there are two more numbers to go through
    for dirty in range(1):
            print(f'You\'ve cleaned {room} room today')
        # but what is this?! range of 1? so it only prints out ONE line of the print and then moves on in the first RANGE?