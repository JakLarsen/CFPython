import math

t = int(input())

for t in range(t):
	a,b = map(int, input().split())
	print(math.ceil(a/b)*b-a)
