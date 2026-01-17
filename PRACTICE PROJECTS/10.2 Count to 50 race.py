counter = 0
stars = "*"

while counter <= 50:
    # print(counter)

    p1 = int(input("P1 choose a number between 1 and 5: "))
    counter += p1
    print(f'Current score {counter}')

    if counter >= 50:
        print("P1 wins!")
        break

    p2 = int(input("P2 choose a number between 1 and 5: "))
    counter += p2
    print(f'Current score {counter}')

    if counter >= 50:
        print("P2 wins!")
        break

