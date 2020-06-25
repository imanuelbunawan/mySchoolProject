
UANG = float(input())
UANG = UANG*100

print("NOTAS:")
if UANG//10000 > 0 :
	print("%i nota(s) de R$ 100.00" %(UANG//10000))
	UANG = UANG%10000
else :
	print("0 nota(s) de R$ 100.00")
if UANG//5000 > 0 :
	print("%i nota(s) de R$ 50.00" %(UANG//5000))
	UANG = UANG%5000
else :
	print("0 nota(s) de R$ 50.00")
if UANG//2000 > 0 :
	print("%i nota(s) de R$ 20.00" %(UANG//2000))
	UANG = UANG%2000
else :
	print("0 nota(s) de R$ 20.00")
if UANG//1000 > 0 :
	print("%i nota(s) de R$ 10.00" %(UANG//1000))
	UANG = UANG%1000
else :
	print("0 nota(s) de R$ 10.00")
if UANG//500 > 0 :
	print("%i nota(s) de R$ 5.00" %(UANG//500))
	UANG = UANG%500
else :
	print("0 nota(s) de R$ 5.00")
if UANG//200 > 0 :
	print("%i nota(s) de R$ 2.00" %(UANG//200))
	UANG = UANG%200
else :
	print("0 nota(s) de R$ 2.00")

print("MOEDAS:")
if UANG//100 > 0 :
	print("%i moeda(s) de R$ 1.00" %(UANG//100))
	UANG = UANG%100
else :
	print("0 moeda(s) de R$ 1.00")
if UANG//50 > 0 :
	print("%i moeda(s) de R$ 0.50" %(UANG//50))
	UANG = UANG%50
else :
	print("0 moeda(s) de R$ 0.50")
if UANG//25 > 0 :
	print("%i moeda(s) de R$ 0.25" %(UANG//25))
	UANG = UANG%25
else :
	print("0 moeda(s) de R$ 0.25")
if UANG//10 > 0 :
	print("%i moeda(s) de R$ 0.10" %(UANG//10))
	UANG = UANG%10
else :
	print("0 moeda(s) de R$ 0.10")
if UANG//5 > 0 :
	print("%i moeda(s) de R$ 0.05" %(UANG//5))
	UANG = UANG%5
else :
	print("0 moeda(s) de R$ 0.05")
if UANG//1 > 0 :
	print("%i moeda(s) de R$ 0.01" %(UANG//1))
	UANG = UANG%1
else :
	print("0 moeda(s) de R$ 0.1")
"""

uang = eval(input())

a = b = c = d = e = f = g = h = i = j = k = l = 0;

uang = float("%2f"%uang)
if int(uang/100)>=1 :
	a = int(uang/100)
	uang = uang%100

uang = float("%2f"%uang)
if int(uang/50)>=1 :
	b = int(uang/50)
	uang = uang%50

uang = float("%2f"%uang)
if int(uang/20)>=1 :
	c = int(uang/20)
	uang = uang%20

uang = float("%2f"%uang)
if int(uang/10)>=1 :
	d = int(uang/10)
	uang = uang%10

uang = float("%2f"%uang)
if int(uang/5)>= 1 :
	e = int(uang/5)
	uang = uang%5

uang = float("%2f"%uang)
if int (uang/2)>=1 :
	f = int(uang/2)
	uang = uang%2


uang = float("%2f"%uang)
if int (uang/1)>= 1 :
	g = int(uang/1)
	uang = uang%1

uang = float("%2f"%uang)
if int(uang/0.5)>= 1 :
	h = int(uang/0.5)
	uang = uang%0.5

uang = float("%2f"%uang)
if int(uang/0.25)>=1 :
	i = int(uang/0.25)
	uang = uang%0.25

uang = float("%2f"%uang)
if int(uang/0.1)>= 1:
	j = int(uang/0.1)
	uang = uang%0.1

uang = float("%2f"%uang)
if int(uang/0.05)>= 1 :
	k = int(uang/0.05)
	uang = uang%0.05

uang = float("%2f"%uang)
if int(uang/0.01)>= 1 :
	l = int(uang/0.01)
	uang = uang%0.01



print("NOTAS:")
print("%d nota(s) de R$ 100.00" % a)
print("%d nota(s) de R$ 50.00" % b)
print("%d nota(s) de R$ 20.00" % c)
print("%d nota(s) de R$ 10.00" % d)
print("%d nota(s) de R$ 5.00" % e)
print("%d nota(s) de R$ 2.00" % f)

print("MOEDAS:");
print("%d moeda(s) de R$ 1.00" % g)
print("%d moeda(s) de R$ 0.50" % h)
print("%d moeda(s) de R$ 0.25" % i)
print("%d moeda(s) de R$ 0.10" % j)
print("%d moeda(s) de R$ 0.05" % k)
print("%d moeda(s) de R$ 0.01" % l)