test_scores = {
    "Alice": 94,
    "Bob": 78,
    "Charlie": 82,
    "Diana": 91,
    "Ethan": 65,
    "Fiona": 88,
    "George": 72,
    "Hannah": 99,
    "Ian": 45,
    "Julia": 83
}

# print(test_scores.keys())
# # this prints out this dict_keys(['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia'])
# # This is iterable
#
# print(test_scores.values())
# # This prints out ONLY the values
# # dict_values([94, 78, 82, 91, 65, 88, 72, 99, 45, 83])
#
# # Iterate
# for student in test_scores.keys():
#     print(student)
#
# total = 0
# for score in test_scores.values():
#     total += score
#     print(total/len(test_scores))

print(test_scores.items())
#  We see that each value is paired
# dict_items([('Alice', 94), ('Bob', 78), ('Charlie', 82), ('Diana', 91), ('Ethan', 65), ('Fiona', 88), ('George', 72), ('Hannah', 99), ('Ian', 45), ('Julia', 83)])

for item in test_scores.items():
    print(item)

# we can unpack the ITEM since it is a PAIR
# example below:

# for key, value in test_scores.items():
#     print(key, value)

# let's find the MAX score below
max_score = 0
best_student = ""
for student, score in test_scores.items():
        if score > max_score:
            max_score = score
            best_student = student
print(f'Highest score was {max_score} by {best_student}')