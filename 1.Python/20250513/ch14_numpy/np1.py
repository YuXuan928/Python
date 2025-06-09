import numpy as np
np1 = np.array([1,2,3,4])	#使用list
np2 = np.array((5,6,7,8))	#使用tuple
print(f'np1=np.array([1,2,3,4]) ➡ 使用list轉array={np1}')
print(f'np2=np.array((5,6,7,8)) ➡ 使用tuple轉array={np2}')
print(type(np1), type(np2))