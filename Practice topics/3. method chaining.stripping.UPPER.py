email = "cheenuethao@gmail.com         "
# print(email)
# This prints out my email

# print(email).strip() OUTPUTS and ERROR
# It gives an error because AFTER python prints out email, it FORGETS what is there so .strip is stripping NOTHING!

new_email = email.strip().upper()
# by creating a new variable called new_email, I'm not tampering with the old variable and I'm able to print out that instead.
# .strip is STRIPPING the LEADING and ENDING white spaces and nothing in between
print(new_email)