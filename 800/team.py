t = int(input())

counter = 0
for t in range(t):
	a,b,c = map(int, input().split())
	if a+b+c > 1:
		counter += 1
print(counter)