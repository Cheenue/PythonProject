# --- 1. SYNTAX ERROR ---
# This happens before the code even runs.
# If I uncomment the line below, the whole script breaks!
def broken_function()
    # This is Missing the colon!


# --- 2. NAME ERROR ---
try:
    print(unknown_variable)
except NameError as e:
    print(f"NAME ERROR: {e} (You haven't defined this variable yet!)")


# --- 3. INDEX ERROR ---
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"INDEX ERROR: {e} (The list isn't that long!)")
#     {e} DOESN'T EXIST!


# --- 4. TYPE ERROR ---
try:
    greeting = "Hello " + 5  # Trying to add a String and an Int
except TypeError as e:
    print(f"TYPE ERROR: {e} (You can't mix those types like that!)")
#     they are NOT the same DATA type


# --- 5. KEY ERROR ---
try:
    scores = {"tim": 91}
    print(scores["carlos"]) # "carlos" isn't a key in the dictionary
except KeyError as e:
    print(f"KEY ERROR: {e} (That key doesn't exist in the dictionary!)")

# --- SUMMARY OF THE FIXES ---
# Syntax: Check your colons, brackets, and indentation.
# Name: Check your spelling.
# Index: Check your list length.
# Type: Use str() or int() to convert data first.
# Key: Use .get() to check dictionaries safely!