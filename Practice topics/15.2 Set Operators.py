# INTERSECTION "&" Operator example

webdev = {'SQL', 'css', 'html', 'javascript', 'python'}
data = {'R', 'python', 'SQL'}
print(webdev & data)
# & shows what is the SAME in both SETS

# UNION "|" OPERATOR

print(webdev | data)
# This prints: {'SQL', 'python', 'css', 'R', 'javascript', 'html'}
# It returns ALL the data from both sets

# DIFFERENCE "-" operator
# ORDER DOES matter

print(webdev - data)
# This prints {'html', 'javascript', 'css'}
print(data - webdev)
# This prints {'R'}
