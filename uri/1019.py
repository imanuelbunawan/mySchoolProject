
N = int(input())
J = N//3600
N = N%3600
M = N//60
N = N%60
D = N
J = str(J)
M = str(M)
D = str(D)
print(f"{J}:{M}:{D}")