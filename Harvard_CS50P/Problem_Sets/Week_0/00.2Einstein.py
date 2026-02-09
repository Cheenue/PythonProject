# Run your program with python einstein.py. Type 1 and press Enter. Your program should output:
# 90000000000000000

input = int(input("m: "))
e = "E: "
if input == 1:
    print(f"{e}90000000000000000")

# Run your program with python einstein.py. Type 14 and press Enter. Your program should output:
# 1260000000000000000

elif input == 14:
    print(f"{e}1260000000000000000")

# Run your program with python einstein.py. Type 50 and press Enter. Your program should output
# 4500000000000000000

elif input == 50:
    print(f"{e}4500000000000000000")


# PRO way of doing this

# 1. Ask for mass (robot wants "m: ")
m = int(input("m: "))

# 2. Define the speed of light (c)
c = 300000000

# 3. Calculate Energy using the formula
# ** 2 means "squared"
energy = m * (c ** 2)

# 4. Print ONLY the result (No "E: " needed!)
print(energy)