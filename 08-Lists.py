# List in Python (similar to array in MATLAB)
# Lists can store different data types
# Lists are mutable; values can be changed and saved

# Creating a list with different data types
matlab_array = [1, 2, 3, 4, 5, 'six', 7.0, True, [8, 9]]
print(f'Original Matlab Array: {matlab_array}')

# Modifying an element in the list
matlab_array[5] = 100
print(f'Updated Matlab Array: {matlab_array}')

# List comprehension to create a new list
x = [1, 2, 3, 4, 5]
y = [num ** 2 for num in x]
print(y)

# Indexing and slicing in lists
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI']
# Forward indexing
print(weekday[1])  # Output: 'TUE'

# Backward indexing
print(weekday[-5])  # Output: 'MON'

# Slicing
print(weekday[1:3])  # Output: ['TUE', 'WED']
print(weekday[-5:-1])  # Output: ['MON', 'TUE', 'WED', 'THU']

print(weekday[1:])  # Output: ['TUE', 'WED', 'THU', 'FRI']
print(weekday[:-3])  # Output: ['MON', 'TUE']
print(weekday[:])  # Output: ['MON', 'TUE', 'WED', 'THU', 'FRI']

# Adding elements to the list
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days.append('SUN')  # Adds 'SUN' to the end of the list
print(days)

month = ['JAN', 'FEB', 'MAR', 'MAY']
month.insert(2, 'APR')  # Inserts 'APR' at index 2
print(month)

# Removing elements from the list
number = [10, 50, 50, 100, 1000]
number.remove(50)  # Removes the first occurrence of 50
print(number)

number = [10, 50, 50, 100, 1000]
number.pop(3)  # Removes the element at index 3
print(number)

number = [10, 50, 50, 100, 1000]
number.pop()  # Removes the last element
print(number)

number = [10, 50, 50, 100, 1000]
number.clear()  # Clears the list
print(number)

number = [10, 50, 50, 100, 1000]
del number[3]  # Deletes the element at index 3
print(number)

number = [10, 50, 50, 100, 1000]
del number[1:4]  # Deletes elements from index 1 to 3
print(number)

number = [10, 50, 50, 100, 1000]
del number  # Deletes the entire list
# print(number) would give an error

# Length of the list
number = [10, 50, 50, 100, 1000, 1000]
print(len(number))

# Iterating over a list
colors = ['Red', 'Blue', 'Green']
for color in colors:
    print(color)

# Checking for an element in a list
if 'white' in colors:
    print('Yes, white is an element of colors.')
else:
    print('No, white is not an element of colors.')

# Creating references and copies of a list
colors = ['Red', 'Blue', 'Green']
mycolor = colors  # Reference to the same list
yourcolor = colors.copy()  # Independent copy of the list
hiscolor = list(colors)  # Another independent copy of the list

print(mycolor)     
print(yourcolor)   
print(hiscolor)

# Modifying the original list
colors.pop()  # Deletes the last element

print(mycolor)     # Reflects the change (same reference)
print(yourcolor)   # Does not reflect the change (independent copy)
print(hiscolor)    # Does not reflect the change (independent copy)
