# Order of operations when it comes to these OPERATORS

# NOT (happens 1st)
# and (then this happens 2nd)
# or (lastly, this happens 3rd)


operator_example = False and True and True
print(operator_example)
# first it checks (False AND True) which is FALSE
# then it checks FALSE AND TRUE, which is FALSE