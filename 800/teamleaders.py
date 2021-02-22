# n = int(input())

# sumNum = 0
# for a in range(1, (n+2)//2, 1):
# 	b = n/a - 1
# 	if (b).is_integer():
# 		sumNum += 1
# print(sumNum)


n = int(input())
sumNum = 0
for a in range(1, (n+2)//2, 1):
	if (n/a-1).is_integer(): sumNum += 1
print(sumNum)