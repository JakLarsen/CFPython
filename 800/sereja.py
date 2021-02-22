n = int(input())
cards = [int(i) for i in input().split()]
serDim = [0, 0]

for i in range(n):
	serDim[i % 2] += max(cards[0], cards[-1])
	if cards[0] > cards[-1]:
		cards = cards[1:]
	else:
		cards = cards[:-1]
print(*serDim)

