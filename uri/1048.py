
Salary = float(input())

if Salary > 0 and Salary <= 400.00 :
	Percent = int(15)
	Bonus = (Salary*(15/100))
	Fix  = Salary + Bonus
elif Salary > 400.00 and Salary <= 800.00 :
	Percent = int(12)
	Bonus = (Salary*(12/100))
	Fix = Salary + (Salary*(12/100))
elif Salary > 800.00 and Salary <= 1200.00 :
	Percent = int(10)
	Bonus = (Salary*(10/100))
	Fix = Salary + (Salary*(10/100))
elif Salary > 1200.00 and Salary <= 2000.00 :
	Percent = int(7)
	Bonus = (Salary*(7/100))
	Fix = Salary + (Salary*(7/100))
elif Salary > 2000.00 :
	Percent = int(4)
	Bonus = (Salary*(4/100))
	Fix = Salary + (Salary*(4/100))

print("Novo salario: %0.2f" %(Fix))
print("Reajuste ganho: %0.2f" %(Bonus))
print("Em percentual:",(Percent),"%")