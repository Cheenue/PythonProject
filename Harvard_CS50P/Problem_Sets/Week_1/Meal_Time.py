def main():
    answer = input("What is the time right now? ")

    # Convert the time string into a decimal float
    time = convert(answer)

    # Breakfast: 7:00 - 8:00
    if 7.0 <= time <= 8.0:
        print("breakfast time")

    # Lunch: 12:00 - 13:00
    elif 12.0 <= time <= 13.0:
        print("lunch time")

    # Dinner: 18:00 - 19:00
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    # Split "7:30" into TWO different STRINGS!
    # "7" and "30"
    hours, minutes = time.split(":")

    # Convert to floats and calculate the decimal
    new_hours = float(hours)
    new_minutes = float(minutes) / 60

    # this CONCATENATES new_hours AND new_minutes
    return new_hours + new_minutes


if __name__ == "__main__":
    main()