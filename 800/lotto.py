n = int(input())
counter = 0

if n//100 > 0:
	counter += n//100
	n -= n//100 * 100
if n//20 > 0:
	counter += n//20
	n -= n//20 * 20
if n//10 > 0:
	counter += n//10
	n -= n//10 * 10
if n//5 > 0:
	counter += n//5
	n -= n//5 * 5
if n//1 > 0:
	counter += n//1
	n -= n//1 * 1

print(counter)