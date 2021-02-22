t = int(input())

for t in range(t):
	n = int(input())
	myLi = []

#take off last number store in array
#take off last second to last, store in array with a 0 etc

# or floor divisions
	for i in range(4,-1,-1):
		if n//(10**i) >= 1:
			myNum = n//10**i * 10**i
			myLi.append(myNum)
			n -= myNum
	print(len(myLi))
	print(*myLi)

