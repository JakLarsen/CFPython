n1 = input()
n2 = input()
newn = ''
for i in range(len(n1)):
	newn += '0' if n1[i] == n2[i] else '1'

print(newn)