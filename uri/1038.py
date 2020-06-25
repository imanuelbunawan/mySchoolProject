X, Y = input().split()
X, Y = int(X), int(Y)

if X == int(1) :
	T = 4.00*Y 
	print("Total: R$ %0.2f" %(T))
elif X == int(2) :
	T = 4.50*Y 
	print("Total: R$ %0.2f" %(T))
elif X == int(3) :
	T = 5.00*Y 
	print("Total: R$ %0.2f" %(T))
elif X == int(4) :
	T = 2.00*Y 
	print("Total: R$ %0.2f" %(T))
elif X == int(5) :
	T = 1.50*Y 
	print("Total: R$ %0.2f" %(T))