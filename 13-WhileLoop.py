value = int(input("Enter the input : "))

i = 0 
while( i <= value):
    if( i == 4):
        i+=1
        continue
    print(i)
    i+=1 
    if( i == value ):
        break