import numpy as np
#一維陣列取值
na = np.arange(0,6)
print(f"na={na}     #全部")                               #[0 1 2 3 4 5]
print(f"na[0]       (#index=0)          = {na[0]}")       #0          
print(f"na[5]       (#index=5)          = {na[5]}")       #5
print(f"na[1:5]     (#index 1-4)        = {na[1:5]}")     #[1 2 3 4]
print(f"na[1:5:2]   (#index 1-4 隔2)    = {na[1:5:2]}")   #[1 3]
print(f"na[5:1:-1]  (#index 5-2 倒行)   = {na[5:1:-1]}")  #[5 4 3 2]
print(f"na[:]       (#全部)             = {na[:]}")       #[0 1 2 3 4 5]  
print(f"na[:3]      (#index 0-2 3之前)  = {na[:3]}")      #[0 1 2]   
print(f"na[::3]     (#index 0-隔3)      = {na[::3]}")     #[0 3]
print(f"na[3:]      (#index 3-最後)     = {na[3:]}")      #[3 4 5]