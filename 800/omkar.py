t = int(input())

for t in range(t):
	n = int(input())
	myLi = [1 for i in range(n)]
	print(' '.join(map(str,myLi)))