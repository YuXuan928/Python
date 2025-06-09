import numpy as np

na0=np.arange(1,16).reshape(3,5)
print(f'\nna0=\n{na0}')

#上段由指令產生同下段
#建立多維陣列
listdata = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]
na = np.array(listdata)
print(f'\nna=\n{na}')
print('na.ndim 維度', na.ndim)
print('na.shape 形狀', na.shape)
print('na.size 數量', na.size)
print()
print(f"na.shape={na.shape} #形狀")    #(3, 5) 
print(f"na.shape[0]={na.shape[0]} #row")   #3 row  
print(f"na.shape[1]={na.shape[1]} #col")   #5 col  
