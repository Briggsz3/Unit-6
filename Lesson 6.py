'''
Name: Zachary Briggs
Date: 12/6/24
TopicsL String Methods
'''

# A method is a function

# upper case
name = "starla"
print(name.upper()) # prints STARLA, doesn't change original string/ doesn't store the copy
print(name) # all lower case.

name = name.upper() # will replace name with STARLA

print(name) # Now you get STARLA

# lower case

name = "FRANKLIN"
print(name.lower()) # prints franklin

# title case (where first letter is capitalized

sentence = "FRANKLIN LEAVE MILLIE ALONE"
print(sentence.title()) # prints Franklin Leave Millie Alone

# swap case
word = "ViOlIN"
print(word.swapcase()) # prints vIoLin (swaps all the cases of each letter)

# strip
school = "         University of        Oregon              "
print(school.strip()) # prints University of         Oregon (strips space at beginning and end)

# find: returns index of first occurence
print("Chicken Burger".find("urg")) # prints 9 (if it doesn't have it, it will print -1


############################################################################
# Boolean checks
print("B".isupper()) # upper case
print("B".islower()) # lower case
print("B".isalpha()) # letter
print("B".isalnum()) # number or letter
print("B".isdigit()) # number