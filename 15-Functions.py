def MyFunction(name):
  print("Welcome to Python Programming! " + name +".")

MyFunction("John")
MyFunction("Marry")
MyFunction("Sam")

def MyFunction(name = "Dude"):
  print("Welcome to Python Programming! " + name +".")

MyFunction()
MyFunction("John")

def MyFunction(num):
  for i in num:
    if (i % 2 == 0):
      print(i ," is an even number.")
    else:
      print(i ," is an odd number.")

MyFunction(range(1,6))

def MyFunction(*num):
  FinalValue = 1;
  for i in num:
    FinalValue = FinalValue * i
  return FinalValue

print(MyFunction(2, 3))
print(MyFunction(2, 3, 5))