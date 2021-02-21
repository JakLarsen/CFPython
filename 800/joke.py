guest = input()
host = input()
check = input()
letters = guest + host
check = sorted(check)
letters = sorted(letters)
''.join(check)
''.join(letters)

def allLettersInString(letters, check):
	return "YES" if letters == check else "NO"

print(allLettersInString(check, letters))