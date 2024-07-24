value = True 
anotherValue = False

print(f"value : {value} type :  {type(value)} another value {value} another value : {type(anotherValue)}")

MyString = ""
print(bool(MyString))

MyList = []
print(bool(MyList))

MyNumber = None
print(bool(MyNumber))


MyString = "Hello"
print(bool(MyString))

MyList = [1, 2, 3]
print(bool(MyList))

MyNumber = 15
print(bool(MyNumber))

MyString = "Hello"
print(MyString.isupper())

# isinstance() function is used to check if an object belongs to specified data type or not.
print(isinstance(MyString, str))