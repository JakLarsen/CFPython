t = int(input())

for t in range(t):
	n = int(input())
	arr = [int(i) for i in input().split()]


	
	if sum(arr) % 2 == 0:
		oddEl = False
		evenEl = False
		
		i = 0
		while not (oddEl == True and evenEl == True) and i < len(arr):
			if arr[i] % 2 != 0:
				oddEl = True
				i += 1
			else:
				evenEl = True
				i += 1

		print(['NO', 'YES'][oddEl == True and evenEl == True])	

	else:
		print("YES")

