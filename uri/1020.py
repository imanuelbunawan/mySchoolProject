W = int(input())
T = W//365
W = W%365
B = W//30
W = W%30
H = W
print("%i ano(s)" %(T))
print("%i mes(es)" %(B))
print("%i dia(s)" %(H))