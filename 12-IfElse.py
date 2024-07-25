i = int(input("enter the number : "))
if  i > 25:
  print(i," is greater than 25.") 
elif i <=25 and i >=10:
  print(i," lies between 10 and 25.") 
else:
  print(i," is less than 10.")

# shorthand condition : <true_value> if <>condition else <false_value>
print(i, "is divisible by 3.") if i % 3 == 0 else print(i, "is not divisible by 3.")