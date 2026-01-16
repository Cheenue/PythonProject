fav_color = "green"
fav_movie = "shrek"
fav_food = "hot dog"

if fav_color == "green":
    print(f"Your favorite color is {fav_color}")
    if fav_food == "sausage":
        print(f"Your favorite food is {fav_food}")
        # this "IF" conditional is NESTED inside the first "IF" conditional meaning that the second "IF" can't happen UNLESS if the first one is true.
        if fav_movie == "shrek":
            print(f"Your favorite movie is {fav_movie}")
            # This conditional cannot happen unless the first two IF conditionals are true.