A = float(input())

if A < 0.00000 or A > 100.00000 :
	print("Fora de intervalo")
elif A <= 25.0000 :
	print("Intervalo [0,25]")
elif A  <= 50.00000 :
	print("Intervalo (25,50]")
elif A <= 75.00000 :
	print("Intervalo (50,75]")
elif A <= 100.00000 :
	print("Intervalo (75,100]")