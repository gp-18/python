# Elements in a set are unordered 
# (no duplicate elements).
# {} syntax
Info = {'John', 25, 'London'}  
print(f"set is : {Info} and type is : {type(Info)}")

#Creating set using constructor
colors = set(('Red', 'Blue', 'Green')) 
print(colors)

weekdays = {'MON', 'TUE', 'WED', 'THU', 'FRI'}

for day in weekdays:
    print(day)

# add() - add an element to the Set.
# update() - add element(s) to the Set. Please note that, Set does not support duplicate elements.

week = {'MON', 'TUE', 'WED'}
week.add('THU')
print(week)

week.update(['FRI', 'SAT'])
print(week)

# remove() - deletes specified element from the Set. Returns an error if the element is not present in the set.
# discard() - deletes specified element from the Set. Returns no error if the element is not present in the set.
# pop() - deletes last element from the Set. Please note that, Set is an unordered data container therefore last element is not predefined.
# clear() - deletes all elements of the set.
# del - deletes the set itself.

number = {10, 50, 100, 1000}
number.remove(50)    #delete 50 from the set.
print(number)

number = {10, 50, 100, 1000}
number.discard(50)   #delete 100 from the set.
print(number)

number = {10, 50, 100, 1000}
number.pop()         #delete last element from the set.
print(number)

number = {10, 50, 100, 1000}
number.clear()        #delete all elements from the set.
print(number)

number = {10, 50, 100, 1000}
del number            #delete set 'number' itself.
# print(number)

# union(): union() method is used to create new set containing set1 and set2.
# update(): update() method is used to add elements of a set in a given set.
colors = {'Red', 'Blue', 'Green'}
numbers = {10, 20}
mySet = colors.union(numbers)
print(mySet)

colors = {'Red', 'Blue', 'Green'}
numbers = {10, 20}
colors.update(numbers)
print(colors)

x = int(input("Enter the number of elements: "))

# Initialize an empty set
sets = set()

# Loop to get each number and add it to the set
for i in range(x):
    # Prompt the user to enter a number at a specific index
    n = int(input(f"Enter the number at index {i}: "))
    # Add the entered number to the set
    sets.add(n)

# Print the resulting set
print("The set of numbers is:", sets)
