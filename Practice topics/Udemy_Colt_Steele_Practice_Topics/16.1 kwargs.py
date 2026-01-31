# **kwargs
# THIS COLLECTS all remaining ARGUMENTS and it has to have a KEY and VALUE

def demo(**kwargs):
    print(kwargs)
#         This prints nothing

# demo(4, True, "goodbye")
# This has to be an ARGUMENT like 'color': red, 'age': 12

demo(color='red', age=20, height=40)

def print_ages(**kwargs):
   for k,v in kwargs.items():
      print(f"{k} is {v} years old")

print_ages(max=67,sue=59,kim=14)
print('*'*50)
# (default parameters, parameters, *args, **kwargs)

# example
def display_info(person, *args, status="single", **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

display_info('Cheenue', 2, 5, 98, 65, 325, 1658, status='FINAL BOSS', age=34, color='black')
# output:
#         person is: Cheenue
#         status is: FINAL BOSS
#         args is: (2, 5, 98, 65, 325, 1658)
#         kwargs is: {'age': 34, 'color': 'black'}

print('*'*50)

display_info(1, 5, 52, 'Cheenue', 2, 5, 98, 65, 325, 1658, status='FINAL BOSS', age=34, color='black')
# output
#           person is: 1
#           status is: FINAL BOSS
#           args is: (5, 52, 'Cheenue', 2, 5, 98, 65, 325, 1658)
#           kwargs is: {'age': 34, 'color': 'black'}

print('*'*50)
def add_thrice(val, lst = []):
    lst.append(val)
    lst.append(val)
    lst.append(val)
    print(lst)

add_thrice(4, [1, 2, 3])
# output: [1, 2, 3, 4, 4, 4]
add_thrice(99)
# output: [99, 99, 99]
#         it added the 99 to that empty list
add_thrice(0)
# output: [99, 99, 99, 0, 0, 0]
#         it added the 0's TO that ALREADY EXISTING list!
print('*'*50)

def add_twice(val, lst = None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    print(lst)

add_twice(42)
# output: [42, 42]
add_twice(64)
# output: [64, 64]
print('*'*50)

def sum_all_nums(a, b, c):
    print(a + b + c)

nums = [1, 2, 3]
# this printed NOTHING
#   BECAUSE IT NEEDS to have 3 things 'a, b ,c'
#   it sees nums = [1, 2, 3] as ONE object of a
#   therefore is need to put *nums
#       LIKE THIS
#           sum_all_nums(*nums)
sum_all_nums(*nums)
# output: 6
