n, k = map(int, input().split())
a = [int(i) for i in input().split()]

c = 0
for i in range(n):
	if a[i] >= a[k-1] and a[i] > 0:
		c += 1
	else:
		break
print(c)

