A, B, C, D = input().split()
A, B, C, D = float(A), float(B), float(C), float(D)

H = ((A*2) + (B*3) + (C*4) + (D*1))/10
print("Media: %0.1f" %(H))

if H >= 7.0 :
	print("Aluno aprovado.")
elif 5.0 <= H <= 6.9 :
	print("Aluno em exame.")
	E = float(input())
	T = (H + E)/2
	print("Nota do exame: %0.1f" %(E))
	if T >= 5.0 :
		print("Aluno aprovado.")
	else :
		print("Aluno reprovado.")
	print("Media final: %0.1f" %(T))
elif H < 5.0 :
	print("Aluno reprovado.")