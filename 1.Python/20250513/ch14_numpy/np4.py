import numpy as np
#linear space => linspace
#linspace()建立等距(差)陣列，返回值為float；第3個參數為個數

a, b, k = 1, 15, 3
na = np.linspace(a, b, k)  #1-15間隔加入3個 1,8,15 
#endpoint bool, optional  是指最後一個數字是否包含進去
#If True, stop is the last sample. Otherwise, it is not included. Default is True.


print("#參數endpoint=True")
print(f"1. 預設endpoint=True：np.linspace({a}, {b}, {k})={na}") #預設endpoint=True
na = np.linspace(a, b, k, endpoint=True) 
print(f"2. np.linspace({a}, {b}, {k}, endpoint=True)={na}") #x=(15-1)/(3-1); 1,1+x,1+2*x
d=(b-a)/(k-1)
na2=np.arange(a, b+1, d, dtype=float)
print(f"3. 自定義間隔 d=(b-a)/(k-1) => d={d}, na2={na2}")


print("\n#參數endpoint=False")
na = np.linspace(1, 15, 3, endpoint=False)  #d=(15-1)/3; 1,1+d,1+2*d
print(f"1. np.linspace(1, 15, 3, endpoint=False)={np.round(na, 2)}")
d=(b-1)/k
na2=np.arange(a, b, d, dtype=float)
print(f"2.自定義間隔 d=((b-1)-a)/(k-1) =>\n {' '*13}x={d} na2={np.round(na2, 2)}")  


print("\n#參數endpoint、retstep") 
na=np.linspace(2.0, 3.0, num=5, endpoint=False)     #endpoint=False
print(f"1. np.linspace(2.0, 3.0, num=5, endpoint=False)：{na}")   #array([2. ,  2.2,  2.4,  2.6,  2.8])
na=np.linspace(2.0, 3.0, num=5, endpoint=True)      #endpoint=True
print(f"2. np.linspace(2.0, 3.0, num=5, endpoint=True)：{na}")   #array([2. ,  2.2,  2.4,  2.6,  2.8])
#參數retstep=True 顯示間隔數 (則會在array的後面，加上間隔多少)
na=np.linspace(2.0, 3.0, num=5, retstep=True)   #retstep=True 顯示間隔數
print(f"3. np.linspace(2.0, 3.0, num=5, retstep=True)-顯示間格：\n{na}")   #array([2.  ,  2.25,  2.5 ,  2.75,  3.  ])
#參數retstep : 預設為False
na=np.linspace(2.0, 3.0, num=5, retstep=False)      #retstep=True 顯示間隔數
print(f"4. np.linspace(2.0, 3.0, num=5, retstep=False)-不顯示間格：\n{na}") 



'''
#linear space => linspace
start       序列的起始值
stop        序列的終止值，如果endpoint為true，該值包含於序列中
num         要生成的等間隔樣例數量，預設為50
endpoint    序列中是否包含stop值，預設為ture
retstep     如果為true，返回樣例，以及連續數字之間的間隔值(多顯示間隔數)
dtype       輸出ndarray的資料類型
'''