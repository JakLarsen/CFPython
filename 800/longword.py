t = int(input())
for t in range(t):
	n = input()
	print ([n, n[0] + str(len(n)-2) + n[-1]][len(n)>10])