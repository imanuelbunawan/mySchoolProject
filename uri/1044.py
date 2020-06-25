A, B = input().split()
A, B = int(A), int(B)

if A%B == 0 or B%A == 0 :
	print("Sao Multiplos")
else :
	print("Nao sao Multiplos")