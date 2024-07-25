# lambda function is also termed as anonymous function and it is a function without a name. An anonymous function is not declared by def keyword, rather it is declared by using lambda keyword.
# lambda parameters: statement

x = lambda a, b : a * b
print(x(3, 4))

MyList = [1, 2, 3, 4, 5]
NewList = list(map(lambda i: i*i, MyList))
print(NewList)


MyList = [1, 2, 3, 4, 5]
NewList = list(filter(lambda i : i%2 == 0 , MyList))
print(NewList)

from functools import reduce
MySet = {10, 20, 30, 40, 50, 60} 
max_num = reduce(lambda a, b: a if a > b else b, MySet)

print(max_num)
