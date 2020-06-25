
A, B, C, D = input().split()
A, B, C, D = int(A), int(B), int(C), int(D)

H = (A*60) + B
G = (C*60) + D

if H > G :
	S = (G+1440) - H
	J = S//60
	M = S%60
	print("O JOGO DUROU",(J),"HORA(S) E",(M),"MINUTO(S)")
elif H < G :
	S = G - H
	J = S//60
	M = S%60
	print("O JOGO DUROU",(J),"HORA(S) E",(M),"MINUTO(S)")
elif H == G :
	S = G - H + 1440
	J = S//60
	M = S%60
	print("O JOGO DUROU",(J),"HORA(S) E",(M),"MINUTO(S)")