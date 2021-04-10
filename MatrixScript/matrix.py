import re
[n,m] = [int(x.strip()) for x in input().split(' ')]
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
chaine = ''
for j in range(m):
	for i in range(n):chaine = chaine + matrix[i][j]
print(re.sub('((?<=\w)\W+(?=\w))', ' ', chaine)) 


