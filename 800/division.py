



n, d = map(int, input().split())


def getFrac(fracNum, den):

	thisDecPlace = 0
	num = fracNum*10
	while num >= den:
		num -= den
		thisDecPlace += 1
		fracNum = num
	return thisDecPlace, fracNum

#ROUNDED DIVISION
def divide(num,den):
	print(f'num/den: {num/den}')
	
	quotient = ''

	wholeNum = 0

	if num >= den:
		fracNum = 0
		while num >= den:
			num -= den
			wholeNum += 1
			fracNum = num
	else:
		fracNum = num

	quotient += str(wholeNum) + '.'
	print(f'quotient so far: {quotient}')
	
	#HOW MANY DECIMAL PLACES FOR FINAL QUOTIENT? <3 = 2
	decPlaces = 0
	while decPlaces < 3:
		quotientPiece, fracNum = getFrac(fracNum, den)
		quotient += str(quotientPiece)
		decPlaces += 1

	#ROUNDING INSTEAD OF TRUNCATION
	if int(quotient[-1]) >= 5:
		quotientLi = []
		quotientLi[:0] = quotient
		quotientLi[-2] = str(int(quotientLi[-2]) + 1)
		quotientLi.pop()
		quotient = ''.join(quotientLi)


	return float(quotient)
	
quotient = divide(n,d)

print(quotient)