n = int(input())
arr = map(int, input().split())
A=[]
B=[]

for i in arr: 
	A.append(i)

for j in A:
	if int(j) < max(A):
		B.append(j)
print(max(B))