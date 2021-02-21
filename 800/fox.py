n,m = map(int, input().split())

right = True
toPrint = ''

for i in range(n):
	if i % 2 == 0:
		toPrint =  '#'*m
		print(toPrint)

	elif right == True:
		toPrint = '.'*(m-1) + '#'
		print(toPrint)
		right = False
	else:
		toPrint = '#' + '.'*(m-1)
		print(toPrint)
		right = True
