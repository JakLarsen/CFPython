t = int(input())

for t in range(t):
	w,h,f = map(int, input().split())

	sheets = 1
	area = w*h

	while area > 0 and area % 2 == 0:
			area /= 2
			sheets *= 2
			
	print(["NO","YES"][sheets >= f])

