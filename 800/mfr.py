from functools import reduce

items = [1,2,3,4,5,6,7,8,9]
squared = list(map(lambda x: x**2, items))
print(squared)
doubled = list(map(lambda x: x*2, items))
print(doubled)

def multiply(x):
	return (x*x)
def add(x):
	return (x+x)

funcs =[multiply, add]

#i = 0,1,2,3,4
for i in range(5):
	multAddArr = list(map(lambda x: x(i), funcs))
	print(multAddArr)


#FILTER
evens = list(filter(lambda x: x%2==0, items))
print(evens)
larger = list(filter(lambda x: x>4, items))
print(larger)


#reduce
product = reduce((lambda nextVal, acc: nextVal*acc), items)
print(product)