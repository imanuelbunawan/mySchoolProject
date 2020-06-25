

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
phi = 3.14159
TRIANGULO = (A*C)/2
CIRCULO = phi*(C**2)
TRAPEZIO = ((A+B)/2)*C
QUADRADO = B**2
RETANGULO = A*B

print("TRIANGULO: %0.3f" %(TRIANGULO))
print("CIRCULO: %0.3f" %(CIRCULO))
print("TRAPEZIO: %0.3f" %(TRAPEZIO))
print("QUADRADO: %0.3f" %(QUADRADO))
print("RETANGULO: %0.3f" %(RETANGULO))