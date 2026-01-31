# WILD CARD *PLACEHOLDER Operator
#       PLACEHOLDER can be any word like args, nums, colors, answers, etc
#       It is OPTIONAL when in a function; It COLLECTS any leftover information

# def average(*args):
#               *args = GATHERS ALL REMAINING ARGUMENTS INTO A TUPLE
#    total = 0
#    for arg in args:
#       total += arg
#    return total/len(args)

# def count_stuff(*nums):
#               You can call it "nums" or anything you like it doesn't matter as long as it's not a word that PYTHON uses
#               In this example, "*nums" will be a TUPLE
#       print(f'You passed me {len(*nums} arguments')


def silly(first, second, *others):
    print(f'\nFirst is: {first}')
    print(f'Second is: {second}')
    print(f'Others is: {others}')

silly(True, False, "Hello", 3, 46, 1246, False, [])
# print("\n")
silly(True, False, "BYE", 4, 75, 3, 28, [])

# Given this (completely useless) function:
#
# def silly_goose(num, *args):
#   return args
# What does silly_goose return when we call silly_goose(1,2,3,4,5)
# It returns (2, 3, 4, 5)