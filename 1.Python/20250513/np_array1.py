import numpy as np

def ShowArrayMsg(a):
    print(f"維度 a.ndim：{a.ndim}")
    print(f"形狀 a.shape：{a.shape}")
    print(f"大小 a.size：{a.size}\n")
    


a = np.arange(15).reshape(3, 5)
print(f"a=np.arange(15).reshape(3, 5)=\n{a}")

'''
a = np.arange(15).reshape(3, 5)
a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
'''

print(f"a.shape(形狀)={a.shape}")  #(3,5)
print(f"a.ndim(維度)={a.ndim}")    #2

print(f"a.dtype.name(資料型態)={a.dtype.name}")   #'int64'
print(f"a.itemsize(每個元素佔用的bytes)={a.itemsize}")       #4 陣列中每個元素佔用的空間 4 bytes
#itemsize是指每一個元素的記憶體使用量，而nbytes是array裡所有元素的記憶體使用量。
print(f"a.size(元素個數)={a.size}")  #15 陣列當中元素的個數
print(f"type(a)={type(a)}")            #<class 'numpy.ndarray'>
print(f"len(a)陣列外層長度={len(a)}\n") #陣列外層長度
ShowArrayMsg(a)


b = np.array([6, 7, 8])
print(f"b=np.array([6, 7, 8])={b}")      #array([6, 7, 8])
print(f"type(b)={type(b)}")            #<class 'numpy.ndarray'>
ShowArrayMsg(b)


print("#--------------------------")
a = np.arange(6)                    # 1d array
print(f"a=np.arange(6)={a}")          #[0 1 2 3 4 5]
ShowArrayMsg(a)

b = np.arange(12).reshape(4, 3)     # 2d array
print(f"b=np.arange(12).reshape(4, 3)=\n{b}")

'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
ShowArrayMsg(b)

c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(f"c=np.arange(24).reshape(2, 3, 4)=\n{c}")

'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''
ShowArrayMsg(c)
