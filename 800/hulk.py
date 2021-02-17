n = int(input())
feelings = ''

for i in range(n):
	snip = 'I hate that ' if i % 2 == 0 else 'I love that '
	feelings += snip

print(feelings[:-5] + "it")



