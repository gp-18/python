# tuples are inmutable 
# matalb agar ek baar assigned hua to change nhi ho skta h 
# syntax for this is ()

tuples = (1,2,3,4,5,6,7,8,9,10)
print(f"tuples : {tuples} type is : {type(tuples)}")

weekday = ('MON', 'TUE', 'WED', 'THU', 'FRI')
#forward indexing
print(weekday[1])

#backward indexing
print(weekday[-1])

Info = ('John', 25, 'London')
#tuple converted into list
Info = list(Info)   
#Making required changes
Info[0] = 'Marry'   
#list converted back to tuple
Info = tuple(Info)  
print(Info)

month = ('JAN', 'FEB', 'MAR')
# returns an error
# month[3] = 'APR'      
# print(month)

month = ('JAN', 'FEB', 'MAR')
# returns an error
# del month[2]          
# print(month)

colors = ('Red', 'Blue', 'Green')
for x in colors :
    print(x)

colors = ('Red', 'Blue', 'Green')
numbers = (10, 20)
mytuple = colors + numbers
print(mytuple)

#this is tuple
color = ('Red',)    
print(type(color))

#this is string
color = ('Red')     
print(type(color))