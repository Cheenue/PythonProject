# Run your program with python nutrition.py. Type Apple and press Enter. Your program should output:
# Calories: 130

item = input("Item: ").lower()

def main():
    fruits = {
        "apple" : 130,
        "avocado" : 50,
        "sweet cherries": 100,
        "tomato" : "",
        "kiwifruit" : 90,
        "pear" : 100
    }

    if item in fruits:
        if fruits[item] != "":
            print(f"Calories: {fruits[item]}")

main()


# Run your program with python nutrition.py. Type Avocado and press Enter. Your program should output:
# Calories: 50


# Run your program with python nutrition.py. Type Sweet Cherries and press Enter. Your program should output
# Calories: 100

# Run your program with python nutrition.py. Type Tomato and press Enter. Your program should output nothing.