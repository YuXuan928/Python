import numpy as np

#ones建立同值陣列 1 (float)
a = np.ones((5,))   
print(f'a = np.ones((5,))：{a}\n')    #一維float

b= np.ones((2, 3), dtype=int)
print(f'b= np.ones((2, 3), dtype=int)：\n{b}\n')     #二維 int

c= np.ones((2, 3, 4), dtype=int)
print(f'c= np.ones((2, 3, 4), dtype=int)：\n{c}')            #三維 int
