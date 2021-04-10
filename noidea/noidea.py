happy=0 ; X={}
for i in range(4):	X[i] = [int(y.strip()) for y in input().split()]
[N,A,B]  = [X[1],set(X[2]),set(X[3])]

for x in N: 
	if x in A:		happy +=  1 
	elif x in B:	happy += -1 
print(happy)