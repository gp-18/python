value = int(input("Enter the value : "))

for i in range(value+1):
    if i == 4 : 
        i+=1
        continue 
    if i == 10 :
        break 
    
    print(i)

for i in range(10):
    print(i)

colors = ['Red', 'Blue', 'Green']
for x in colors:
  print(x)

word = 'python'
for letter in word:
  print(letter)

dict = {
  'year': '2000',
  'month': 'March',
  'date': 15
}

for day, value in dict.items():
  print(day,value)