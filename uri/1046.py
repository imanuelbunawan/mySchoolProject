

A, B = input().split()
A, B = int(A), int(B)

if A > B :
	H = (24-A)+B
	print("O JOGO DUROU %i HORA(S)" %(H))
elif B > A :
	H = B - A
	print("O JOGO DUROU %i HORA(S)" %(H))
elif B == A :
	H = (A+24)-B
	print("O JOGO DUROU %i HORA(S)" %(H))