def IsPrime(n):
	for x in range(2, int(n / 2) + 1):
		if not x % n:
			return False
	return True

def PrimesTo(n):
	for x in range(2, n):
		if IsPrime(x):
			print(x)