# list matlab simple array [] different data types bhi store ho skte h ismai 
# lists are mutable unmai value change kaaro to value change hoti h and save hoti h 

matlab_array = [1, 2, 3, 4, 5, 'six', 7.0, True, [8, 9]]
print(f'Original Matlab Array: {matlab_array}')

matlab_array[5] = 100
print(f'Original Matlab Array: {matlab_array}')

x = [ 1, 2, 3, 4, 5]
y = [ x ** 2 for x in x ]
print(y)


weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI']
            # 0     1     2       3      4
            #-5    -4    -3      -2     -1           
#forward indexing
print(weekday[1]) 

#backward indexing 
print(weekday[-5])  

# left side index include hota h right side wala index include nhi hota h 
print(weekday[1:3])
print(weekday[-5:-1],"\n")

print(weekday[1:])
print(weekday[:-3],"\n")
print(weekday[:])


# to add new element 
# append new element at last 
# insert at specified index
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# add this element in last of the list
days.append('SUN')   
print(days)

month = ['JAN', 'FEB', 'MAR', 'MAY']
# add 'APR' at index=2 of the list
month.insert(2,'APR') 
print(month)

# remove() - deletes first occurrence of a specified element from the list.
# pop() - deletes element at specified index or last element if index is not specified.
# clear() - deletes all elements of a list.
# del - deletes a element or range of elements or list itself.

number = [10, 50, 50, 100, 1000]
#delete first occurrence of 50.
number.remove(50)    
print(number)

number = [10, 50, 50, 100, 1000]
#delete element at index=3.
number.pop(3)        
print(number)

number = [10, 50, 50, 100, 1000]
#delete last element from the list.
number.pop()        
print(number)

number = [10, 50, 50, 100, 1000]
#delete all elements from the list.
number.clear()     
print(number)

number = [10, 50, 50, 100, 1000]
#delete element at index=3.
del number[3]       
print(number)

number = [10, 50, 50, 100, 1000]
#delete element at index=1,2 and 3.
del number[1:4]     
print(number)

number = [10, 50, 50, 100, 1000]
#delete list 'number'.
del number          
# print(number) gives error

number = [10, 50, 50, 100, 1000, 1000]
print(len(number))

colors = ['Red', 'Blue', 'Green']
for x in colors:
    print(x)
    
colors = ['Red', 'Blue', 'Green']
if 'white' in colors:
  print('Yes, white is an element of colors.')
else:
  print('No, white is not an element of colors.')   
  
# = operator: Creates a reference of the list. Any change in old list modifies new list also.
# copy(): Creates an independent copy of a list.
# list(): Creates an independent copy of a list.     

colors = ['Red', 'Blue', 'Green']
mycolor = colors
yourcolor = colors.copy()
hiscolor = list(colors)

print(mycolor)     
print(yourcolor)   
print(hiscolor, "\n")    

#delete last element in 'colors'
colors.pop()       

print(mycolor)     
print(yourcolor)   
print(hiscolor)  