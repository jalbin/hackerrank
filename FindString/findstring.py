import re
 
a = 'ABCDCDC'
pattern = 'CDC'

A = re.sub(pattern,"U",a,2)

print(A)

