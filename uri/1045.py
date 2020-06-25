A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
if A >= B >= C :
	X = A
	Y = B
	Z = C
elif B >= C >= A :
	X = B
	Y = C
	Z = A
elif C >= A >= B :
	X = C
	Y = A
	Z = B
elif A >= C >= B :
	X = A
	Y = C
	Z = B
elif B >= A > C :
	X = B
	Y = A
	Z = C
elif C >= B >= A :
	X = C
	Y = B
	Z = A
else :
	X = X
	Y = Y
	Z = Z

if X >= Y+Z :
	print("NAO FORMA TRIANGULO")
else :
	if X**2 == (Y**2) + (Z**2) :
		print("TRIANGULO RETANGULO")
	if X**2 > (Y**2) + (Z**2) :
		print("TRIANGULO OBTUSANGULO")
	if X**2 < (Y**2) + (Z**2) :
		print("TRIANGULO ACUTANGULO")
	if X == Y == Z :
		print("TRIANGULO EQUILATERO")
	if X == Y != Z or Y == Z != X or X == Z != Y :
		print("TRIANGULO ISOSCELES")




