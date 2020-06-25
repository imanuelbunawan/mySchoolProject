A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if (A + B) > C and (A + C) > B and (B + C) > A :
	K = A+B+C
	print("Perimetro = %0.1f" %(K))
else :
	A = ((A+B)/2)*C
	print("Area = %0.1f" %(A))