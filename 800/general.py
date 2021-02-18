n = int(input())
a = [int(i) for i in input().split()]

numMax = 0
maxId = 0
numMin = 999
minId = 0
moves = 0
for i in range(n):
	if a[i] > numMax:
		numMax = a[i]
		maxId = i
	if a[i] <= numMin:
		numMin =  a[i]
		minId = i
moves = n-1-minId + maxId
if minId < maxId:
	moves -= 1
print(moves)
