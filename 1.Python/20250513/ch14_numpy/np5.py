import numpy as np
#zeros()建立同值陣列 0 (float)
a = np.zeros((5,))  #一維float
print(a)

b= np.zeros((2, 3), dtype=int)
print(b)            #二維 int

c= np.zeros((2, 3, 4), dtype=int)
print(c)            #三維 int