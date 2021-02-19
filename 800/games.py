# n(n-1) - looking for host uniform = guest uniform

n = int(input())

myLiHome = []
myLiAway = []
for team in range (n):
	a,b = map(int, input().split())
	myLiHome.append(a)
	myLiAway.append(b)

conflicts = 0

for i in range(len(myLiHome)):
	if myLiHome[i] in myLiAway:
		conflicts += myLiAway.count(myLiHome[i])
print(conflicts)

