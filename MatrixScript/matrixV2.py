import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

chaine = ''
for j in range(m):
	for i in range(n):
		chaine = chaine + matrix[i][j]

mypattern = '((?<=\w)\W+(?=\w))'
result = re.sub(mypattern, ' ', chaine) 

print(result)