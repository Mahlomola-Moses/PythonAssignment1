#####################################
#### EXERCISE 1 30 MARKS#######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 - 10 Points##
###############

# Given the string:
s = 'fullstackslp'

# Use indexing to print out the following:

# 'f'
#ans
print(s[0])

# 'p'
#ans
print(s[-1])

# 'stack'
#ans
print(s[4:9])

# 'slp'
#ans
print(s[9:])

# 'cks'
#ans
print(s[7:10])

# Bonus: Use indexing to reverse the string

#ans
print(s[::-1])
###############
## Problem 2 - LISTS - 5 Marks##
###############

# Given this nested list:
l = [3,7,[5,[1,4,'hello']]]
# Reassign "hello" to be "goodbye"
print("")
#ans
print(l[2][1][2])

###############
## Problem 3 - DICTIONARIES - 6 Marks##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print("")
#ans
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
#ans
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0])
###############
## Problem 4 - SETS - 4 Marks##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print("")
print(set(mylist))

###############
## Problem 5  - FORMATTING - 5 Marks##
###############

# You are given two variables:
age = 45
name = "Kyle"

# Use print formatting to print the following string:
#"Hello my dog's name is Kyle and he looks 45 years old"
print( "Hello my dog's name is {} and he looks year old {}" .format(name,age))
