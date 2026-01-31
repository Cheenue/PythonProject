from itertools import count

email_subjects = ["sports", "food", "alphabet", "pets", "activities"]

# for subject in email_subjects:
#     print("Sending EMAIL SUBJECT: ")
#     print(subject)

count = 0

while count < len(email_subjects):
    print("Hello team, the subject of the day is: ")
    print(email_subjects[count])
    count += 1