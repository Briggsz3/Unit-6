'''
Name: Zachary Briggs
Date: 12/2/2024
Topics: Indexing, Slicing, Immutability
'''

# Review
name = "Starla" # a string literal
age = 5

# f-strings (formated strings)
description = f"{name} likes wand toys"
print(description)

# same result with concatenation
description = name + " likes wand toys and is " +str(age + 1) + " next year " # you can do math
print(description)

# indexing - every character has a location
# starting at 0 from the beginning or -1 at the end

# 0  1  2  3  4  5
# S  t  a  r  l  a
#-6 -5 -4 -3 -2 -1

first_letter = name[0] # always use 0 if you don't know the length
print(first_letter) # prints the first letter (S)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1*len(name)] # if you don't know the length (prints: S)
print(first_letter)

last_letter = name[-1] # prints a (from starla), use if you don't know the length
print(last_letter)
last_letter = name[len(name)-1] # prints a (from Starla)
print(last_letter)

# use [] to access a character not () - gives TypeError
# accessing a positive index that does not exist gives IndexError ex: print(name[20])
# there aren't 20 letters of starla
#print(name[20])  # doesn't print anything
#print(name[-20]) # doesn't print anything

# can avoid this by
try:
    print(name[20])
except IndexError:
    print("Out of bounds")
# This stops the code from crashing

# HW for Lesson 1 is 7.1.5 & 7.1.6

###########################################################################]
# Slicing - used to access 1 or more characters in a string
# Instead of name[0]+name[1]+name[2] we can do name[0:3]

# first three letters
first_three = name[0]+name[1]+name[2]
print(first_three)
first_three = name[0:3] # start at index 0, go up to but not include 3
print(first_three)

# Format
# string_name[start: stop: step] - none are technically required

word_one = "Adventure"
# What is the result of print(word_one[3:])
# Try leaving out start, both and try - indecies
print(word_one[0:]) # prints Adventure
print(word_one[:0]) # prints an empty line
print(word_one[3:]) # prints enture
print(word_one[:3]) # prints Adv
print(word_one[:]) # prints Adventure
print(word_one[-6:-1]) # prints entur
print(word_one[-1:]) # prints e
print(word_one[:-1]) # prints Adventur (no e)
print(word_one[:5000]) # prints Adventure
print(word_one[5000:]) # prints an empty line
print(word_one[-5:-2]) # prints ntu
 # default values  start = 0, stop = -1, step = 1
print(word_one[::-1]) # prints erutnevdA
print(word_one[::2]) # prints Avnue
# - step is left (for step values)
# + step is right  ~~~~~~~~~~~
print(word_one[-3:-7:-2]) # prints un
print(word_one[-7:-3:-2]) # doesn't print anything because it has it counting left (becoming more -)
# if step is positive then the start has to be less that step
# parameters doesn't allow it to work

# HW for Lesson 2 is 7.2.6 - 7.2.8

#########################################################################################



