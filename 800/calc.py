n = int(input())
print(n//2 if n % 2 == 0 else int(-n/2 - 0.5))
#FLOOR DIVISION WITH NEGATIVES ROUNDS DOWN STILL, NOT TRUNCATION