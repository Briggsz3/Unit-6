'''
Name: Zachary Briggs
Date: 12/4/2024
Topics: Immutability, for loops, in keyword
'''
# can't mutate/ change strings cat_name[5] = "ie" doesn't work
cat_name = "Franklin"
cat_name = cat_name[0:5]+"ie"
print(cat_name)


##### for loop ####

# Traversing a string
# Non-Pythonic way
cat_name = "Winston"
for i in range(len(cat_name)):
    print(cat_name[i])
# prints a letter on a new line.
print(" ")

for i in range(len(cat_name)):
    print(cat_name[i])
    if cat_name[i] == "n":
        break
# Prints Win on different lines
print(" ")
# The in keyword
vowels = "aeiou"
print("a" in vowels) # Prints True
print("b" in vowels) # Prints False

print(" ")

for i in range(len(cat_name)):
    if cat_name[i] in vowels:
        print(cat_name[i])
# Prints io on diff lines

print(" ")
print("win" in cat_name) # False because the w isn't capitalized

print(" ")

# Use 2 - Pythonic Traversal
# Letter is like i
cat_name = "Millie"
for letter in cat_name:
    print(letter)
# Prints Millie

print(" ")

large_number = 23456788765
for digit in str(large_number): # breaks if no str() is involved
    print(digit, end=" ")

print("\n------") # breaks if no \n involved
print(str(123) in str(12345)) # Prints True