
from itertools import groupby
data=input()
groups = []
result=[]
for k, g in groupby(data):
    groups.append(list(g))
for i in groups:
    result.append((len(i),int(i[0])))

for i in result:
    print(i,end=' ')
    
    
    
    
