n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

if 0 not in set(a+b):
	levelsCleared = len(set(a+b))
else:
	levelsCleared = len(set(a+b)) - 1
print(["Oh, my keyboard!", "I become the guy."][levelsCleared == n])

