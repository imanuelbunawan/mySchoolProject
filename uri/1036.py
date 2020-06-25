from math import sqrt
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A > 0 and B > 0 and C > 0 :
	dis = B**2 - 4*A*C
	if dis > -1 :
		x1 = (-B + sqrt(dis)) / (2*A)
		x2 = (-B - sqrt(dis)) / (2*A)
		print("R1 = %0.5f" %(x1))
		print("R2 = %0.5f" %(x2))
	else :
		print("Impossivel calcular")

else :
	print("Impossivel calcular")