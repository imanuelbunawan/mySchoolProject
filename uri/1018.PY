UANG = int(input())

print(UANG)
if UANG//100 > 0 :
	print("%i nota(s) de R$ 100,00" %(UANG//100))
	UANG = UANG%100
else :
	print("0 nota(s) de R$ 100,00")
if UANG//50 > 0 :
	print("%i nota(s) de R$ 50,00" %(UANG//50))
	UANG = UANG%50
else :
	print("0 nota(s) de R$ 50,00")
if UANG//20 > 0 :
	print("%i nota(s) de R$ 20,00" %(UANG//20))
	UANG = UANG%20
else :
	print("0 nota(s) de R$ 20,00")
if UANG//10 > 0 :
	print("%i nota(s) de R$ 10,00" %(UANG//10))
	UANG = UANG%10
else :
	print("0 nota(s) de R$ 10,00")
if UANG//5 > 0 :
	print("%i nota(s) de R$ 5,00" %(UANG//5))
	UANG = UANG%5
else :
	print("0 nota(s) de R$ 5,00")
if UANG//2 > 0 :
	print("%i nota(s) de R$ 2,00" %(UANG//2))
	UANG = UANG%2
else :
	print("0 nota(s) de R$ 2,00")
if UANG//1 > 0 :
	print("%i nota(s) de R$ 1,00" %(UANG))
else :
	print("0 nota(s) de R$ 1,00")

