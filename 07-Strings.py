# Remember strings are immutable, meaning they cannot be changed. The original string remains the same.
# You need to think about memory references.

string = "this is the string"

multiLineString = """this is the 
multi-line string
can go to multiple lines"""

print(f"this is the string: {string} and this is the multi-line string: {multiLineString}")

ordering = "Parth"
print(ordering[0], ordering[1], ordering[2], ordering[3], ordering[4])
print(ordering[-1], ordering[-2], ordering[-3], ordering[-4], ordering[-5])

# In slicing, remember the left side is included, and the right side is not included
# 0 1 
print(ordering[0:2])  # This prints 'Pa'
# The slicing ordering[-1:-3] won't work as intended because in negative slicing, you need to specify the step as -1 to reverse the direction.
# Hence, ordering[-1:-3:-1] is used to get the characters in reverse order: 'ht'.
print(ordering[-1:-3:-1])
# -1 to reverse the direction
print(ordering[:-5:-1])  # This prints 'htraP'
print(ordering[:])  # This prints the whole string 'Parth'
print(f"The length of the string is {len(ordering)} characters")  # Prints the length of 'Parth', which is 5
print("p" in ordering)  # Prints False, as 'p' is not in 'Parth'
print("P" in ordering)  # Prints True, as 'P' is in 'Parth'

text_1 = 'Learn'
text_2 = 'Python'
MyString = text_1 + text_2
print(MyString)  # Prints 'LearnPython'

MyString = text_1 + " " + text_2
print(MyString)  # Prints 'Learn Python'

# Demonstrate various string methods
# lower(): Returns string in lowercase
# upper(): Returns string in uppercase
# strip(): Removes whitespaces from start and end of the string
# replace(): Replace specified character(s) with another specified character(s)
# split(): Split the string by specified separator and returns substrings in a list.
# count(): Returns number of occurrences of specified character(s) in the string

# Strings are immutable, meaning they cannot be changed.
print(f"ordering before upper(): {ordering}")
ordering.upper()
print(f"ordering after upper(): {ordering}")

# Since strings are immutable, the original string remains the same
print(f"ordering before upper(): {ordering}")
orderingUpper = ordering.upper()
print(f"ordering after upper(): {ordering} and storing into new variable {orderingUpper}")

print("lower():", ordering.lower())  # Prints 'parth'
print("upper():", ordering.upper())  # Prints 'PARTH'

name = "           name                   "
print(f"name without strip: '{name}'")
print(f"name with strip: '{name.strip()}'")  # Prints 'name' without leading and trailing spaces

MyString = "Learn Python"
print(MyString.replace("Python", "C++"))  # Prints 'Learn C++'

splitMyString = MyString.split(" ")
print(splitMyString)  # Prints ['Learn', 'Python']

# Corrected the join operation
joinMyString = " ".join(splitMyString)
print(joinMyString)  # Prints 'Learn Python'

# count does not work with substring
MyString = "cdcdc"
print(MyString.count('cdc')) 
