import numpy as np
a1=np.array(list(map(int,input().split())))
a2=np.array(list(map(int,input().split())))
print(np.inner(a1,a2))
print(np.outer(a1,a2))
