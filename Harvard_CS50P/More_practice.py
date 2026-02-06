# # replace()
#
# my_thoughts = "In recent years, many people have become increasingly aware of the need for physical fitness.* Almost everywhere people turn, whether it is to a newsstand, television or billboard,* advise for guarding and improving health bombards them. Although much of this advice is commercially motivated by those eager to sell vitamins, natural foods and reducing gimmicks,* some of it, especially those advocating a regular exercise program, merits serious attention. Such a program, if it consists of at least 30 minutes three times a week and if a person’s physician approves it,* provides numerous benefits. Regular exercise releases tension, improves appearance, and increases stamina."
#
# my_thoughts = my_thoughts.replace("a","_")
#
# print(my_thoughts)
#
# print("*" * 50)
#
# # THE BORING WAY
# mall = input("How much do you want to spend today at the mall? ")
# mall_a = mall.replace("$","")
# mall_b = float(mall_a)
# print(mall_b)
#
# print("*" * 50)
#
# # the cleaner way!
# mall2 = float(input("How much do you want to spend today at the mall? ").replace("$", ""))
#
# print(f'$ {mall2:.2f}')
#
# print("*" * 50)

def main():
    clean_total = total_to_float(input("How much did you spend today? "))

    # this is asking how much tip did they pay
    tip_max = total_tip(input("How much was the tip? "))

    # this is finding the tip total from all the shopping
    tips = clean_total * tip_max

    # this turned TIPS into a float
    # exact_tips = float(f"{tips:.2f}")
    # this code line was redundant


    total_amount = clean_total + tips
    print(f"Grand Total: $ {total_amount:.2f}")

def total_to_float(t):
    tofla = t.replace("$","")
    return float(tofla)

def total_tip(ip):
    tifla = ip.replace("%","")
    return float(tifla) / 100

main()