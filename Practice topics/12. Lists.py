# store = ["apple", "orange", "berry"]
#
# rand = [2, 5, 62, "hello", []]
# # this is also a valid list with different types of things in the list
#
# stuff = list(range(3, 10))
# print(stuff)
#
# ***********************************************************************************
#
# waitlist = ['john', 'tom', 'sally', 'steve']
# print(waitlist[2])
# print(len(waitlist))
# print(waitlist[-3])
# # this printed off an index from the waitlist list by using brackets
# # i can also fine the LENGTH of the waitlist which i believe is the NUMBER of items in the LIST CONTAINER
# # when it was a NEGATIVE number in the bracket, it started off from the first index which is zero and moved back from the last on the list.
#
# ***********************************************************************************
#
# waitlist[2] = 'joy'
# print(waitlist)
# # here, i CHANGED the list index 2 to 'joy' but if i ran the entire code the first waitlist[2] would show sally and NOT joy and this tells me that python does the code from top to down
#
# ***********************************************************************************
#
# print(waitlist[5])
# # this prints out ERROR List index out of range
# waitlist[4] = "Gomez"
# print(waitlist)
# # this does NOT print out Gomez
# # this tells us that we can access a slot NOT in the container but we CAN'T change slots with the [] and setting it equal to something. There are other ways to ADD to the list it's just not this way
#
# ***********************************************************************************
# APPEND()
# waitlist.append('mike')
# print(waitlist)
# # this added mike to the END of the list
#
# people = ['cheenue', 'seng', 'hlee']
#

# # waitlist.append(people)
# # print(waitlist)
# # this added the CONTAINER to the end of the list
# # result was ['john', 'tom', 'sally', 'steve', 'mike', ['cheenue', 'seng', 'hlee']] which is NOT what I wanted to do
#
# ***********************************************************************************

# EXTEND()
# waitlist.extend(people)
# print(waitlist)
# # by EXTENDING the list I am ADDING the CONTENTS of the list TO my existing list

# ***********************************************************************************

# INSERT()
# num = [3, 4, 5]
# num.insert(1, 8)
# print(num)
# so INSERTING 8 will be BEFORE the index of 1
# 8 will be the NEW index of 1

# ***********************************************************************************

# List SLICES()
# nums = [4, 5, 6, 7]
# print(nums[1:3])
# this prints out starting at index 1 which is 5 and then prints out index 2 which is BEFORE index 3
# this printed [5, 6]
# nums[1:3] = 'a', 'b', 'c'
# print(nums)
# however for this one it printed this
# [4, 'a', 'b', 'c', 7]

# ***********************************************************************************

# CLEAR, REMOVE and POP()

people = ['kyle', 'woody', 'jj', 'seville', 'simba', 'woody']
# print(people.clear())
# this CLEARS people to give the output NONE

# people.remove('woody')
# print(people)
# this printed REMOVED the FIRST time we see woody in the code line
# when using REMOVE() it has to be EXACTLY what you want removed

print(people.pop(0))
# by putting NOTHING in the POP(), it will remove the LAST item in the list and it RETURNS it
print(people)
# but when i print people it doesn't RETURN it though...
# it just prints this ['kyle', 'woody', 'jj', 'seville', 'simba']