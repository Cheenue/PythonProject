# input = float(input("How much was the meal? "))
# second_input = float(input("What percentage would you like to tip? "))
# p = float(f'Leave: $')
#
# tip = (f'{m * (o/100)}')
#
# q = round(tip, 2)
#
# print(q)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dofla = d.replace("$", "")
    return float(dofla)


def percent_to_float(p):
    # TODO
    clefla = p.replace("%", "")
    return float(clefla) / 100

main()