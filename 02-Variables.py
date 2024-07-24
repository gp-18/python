x , y = ["a", "b", "c", "d"] , ("a", "b", "c", "d")
print(f"{type(x)}")
print(f"{type(y)}")

# cause error
# a = "john"
# b = 5
# print(a+b)

# correct 
a = "john"
b = str(5)
print(a+b)

MyStr = "Hello World!"
def MyPrint():
  MyStr = "Hello John!"
  print(MyStr)

#variable accessed inside function
MyPrint()
#variable accessed outside function
print(MyStr)
