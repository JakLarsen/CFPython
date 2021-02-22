n = int(input())

#if even, prints 8 , n - 8, which = n
#if odd, prints 8 , n - 8, which equals n
print(8 + n % 2, n - 8 - n % 2)
