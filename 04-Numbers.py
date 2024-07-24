MyInt = 10
print(type(MyInt))

MyFloat = 10.5
print(type(MyFloat))

MyComplex = 5 + 5j
print(type(MyComplex))


addOfMyIntAndMyFloat = MyInt + MyFloat 
addOfMyFloatAndMyComplex = MyComplex + MyFloat

print(f"{addOfMyIntAndMyFloat} and type is {type(addOfMyIntAndMyFloat)}")
print(f"{addOfMyFloatAndMyComplex} and type is {type(addOfMyFloatAndMyComplex)}")