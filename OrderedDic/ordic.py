import collections
import re

od=collections.OrderedDict() ; A=[]

for i in range(int(input())): A.append(input())
count = dict(collections.Counter(A))  

for j in A: [name,price] = [re.findall(".*[^\s\d+]", j)[0],re.findall("\d+", j)[0]] ; od[name] = price

for k in count.keys(): item = re.findall(".*[^\s\d+]", k)[0] ; print(item,int(od[item])*int(count[item + ' ' + od[item]]))