# Python 3 implementation to Divide two
# integers without using multiplication,
# division and mod operator

def divide(dividend, divisor): 
 
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
     
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor): 
        dividend -= divisor
        quotient += 1
     
     
    return sign * quotient
 
 
# Driver code
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))
a = 1
b = 8
print(divide(a, b))
