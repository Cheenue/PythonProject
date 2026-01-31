counter = 30

print("Welcome to the game!\n" + "*" * 25)
P1 = input("Player 1, what is your name? ")
P2 = input("Player 2, what is your name? ")

while counter > 0:
    p1 = int(input(f"{P1}, choose a number between 1 and 3: "))
    # THE TRAP STARTS HERE
    while p1 < 1 or p1 > 3:
        p1 = int(input("Cheater! You must choose 1, 2, or 3: "))
    # THE TRAP ENDS HERE
    counter -= p1

    if counter < 1:
        print(f"{P1} wins!")
        break

    print(counter)
    # I had to put this here because if I didn't then the output would show only P1 and P2 choosing a number to subtract from the counter but what if P1 made it to 0 already

    p2 = int(input(f"{P2}, choose a number between 1 and 3: "))
    counter -= p2

    if counter < 1:
        print(f"{P2} wins!")
        break

    print(counter)