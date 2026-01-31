# len("hello")
# # we know this as 5 characters but if we run it, it won't print anything out
#
# num = len("hello")
# # this will put that 5 into a defined variable
#
# print(num)

# ***********************************************************************************

# def divide(a, b):
#     print(a/b)
#
# divide(10,50)
#
# result = divide(10,50)
# # Python did what was in the parameters for DIVIDE however since DIVIDE has a PRINT() in the function, it printed the result, threw away the result and left NOTHING to be given back to the object RESULT
#
# print(result)

# ***********************************************************************************

# whenever you return a function, it STOPS the execution of that function

def divide(a, b):
    return a / b

result = divide(1, 2)

print(result)