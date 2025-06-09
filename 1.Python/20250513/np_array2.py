# -*- coding: utf-8 -*-
import numpy as np
#from numpy import *


a = np.array([1, 2, 3, 4])     #一維陣列建立
b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype = float)  #二維陣列建立
c = np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [(2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype = float)  #三維陣列建立
print(f'若b=\n{b}', end='')
print(f'\n則b[[1, 1, 0, 0], [0, 2, 1, 0]]=>index：(1,0),(1,2),(0,1),(0,0) =\n{b[[1, 1, 0, 0], [0, 2, 1, 0]]}')


#Fancy Indexing 指傳遞索引陣列以便一次得到多個陣列元素。
print('\n#(一)、一維陣列的 Fancy Indexing')
#(1)索引列表
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f'x={x}')
#select elements at index 1, 2, 5, 7
sel_idx = [1, 2, 5, 7]
print(f'#(1)索引列表(Fancy Indexing)：\n若sel_idx = [4], 則x[4]={x[4]}') 
print(f'若sel_idx = [1, 2, 5, 7], 則x[sel_idx]={x[sel_idx]}') 


#(2)布林索引陣列
x = np.arange(5)    #Out: array([0, 1, 2, 3, 4])
print(f'\nx={x}')
index = [True, True, False, False, True]
# 取得布林索引陣列元素為true對應索引(0, 1, 4)所形成的陣列
print(f'#(2)布林索引陣列：\n若index = [True, True, False, False, True], 則x[index]={x[index]}')    #array([0, 1, 4])


print('\n#(二)、二維陣列的 Fancy Indexing')
x = np.arange(16)
y = x.reshape(4, -1)    #陣列切割 Array Slicing
print(f'x=np.arange(16)=\n{x}')
print(f'y=x.reshape(4, -1)=\n{y}')
'''
Out: array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
'''
row = np.array([0, 1, 2])
col = np.array([1, 2, 3])
# (0, 1), (1, 2), (2, 3) 所形成的一維陣列
print(f'\n則row=np.array([0, 1, 2])={row}') 
print(f'則col=np.array([1, 2, 3])={col}') 
print(f'則y[row, col]={y[row, col]} #取(0,1), (1,2), (2,3)')  #array([ 1,  6, 11])

print(f'則y[0, col]={y[0, col]}')  #array([ 1,  2, 3])

print(f'則y[:2, col]=\n{y[:2, col]}')   

col = [True, False, True, True] #布林索引陣列
print('\n#(三)、布林索引陣列\n如 col=[True, False, True, True], 則：')
print(f'y[1, col]={y[1, col]}')    #Out: array([4, 6, 7])

print('\n#(四)索引及切片')
a = np.array([[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10], 
              [11, 12, 13, 14, 15], 
              [16, 17, 18, 19, 20], 
              [21, 22, 23, 24, 25]])
print(f'a=\n{a}')              
b = a[(0, 1, 2, 3, 4), (1, 1, 2, 3, 4)] # 取出(0,1),(1,1),(2,2),(3,3),(4,4)的元素(藍色圈圈)
c = a[2:, [0, 2]] # 取出第2+1列以後，第0+1行及第2+1行的所有元素(紅色圈圈)
d = a[3:, 3:] # 取出第3+1列以後，第3+1行以後的所有元素(綠色圈圈)

print(f'\n若b=a[(0, 1, 2, 3, 4), (1, 1, 2, 3, 4)]\n則b={b} #取(0,1),(1,1), (2,2),(3,3),(4,4)')
print(f'\n若c=a[2:, [0, 2]] # 取出第2+1列以後，第0+1行及第2+1行的所有元素 \n則c=\n{c}')
print(f'\n若d=a[3:, 3:] # 取出第3+1列以後，第3+1行以後的所有元素\n則d=\n{d}')


#----------
list_data =[
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]],
    [[14, 18, 13, 12],
     [25, 26, 27, 28],
     [39, 30, 31, 32],
     [43, 44, 45, 46]],
]

numpyArray = np.array(list_data)
print("維度:", numpyArray.ndim)
print("形狀:", numpyArray.shape)
print("數量:", numpyArray.size)
print('\n#(五)多維取值')
print(f'#印出全部：numpyArray[::]=\n{numpyArray[::]}') # 印出全部
print(f'#取出部份1：numpyArray[1, 3, 2]={numpyArray[1, 3, 2]} # matrix:1, row:3, col:2') # matrix:1, row:3, col:2, result:45
print(f'#取出部份2：numpyArray[0, 1:3, 3]={numpyArray[0, 1:3, 3]} # matrix:0, row:1,2, col:4') # matrix:1, row:3, col:2, result:[ 8 12]
print(f'#取出部份3：numpyArray[:, 1:3, 3]=\n{numpyArray[:, 1:3, 3]} #matrix:all, row:1,2, col:3') # matrix:all, row:3, col:2, result:[[ 8 12] [28 32]]


#--------
print('\n#(六)矩陣相乘')
a = np.arange(8).reshape(2,2,2) 
b = np.arange(4).reshape(2,2) 
print(f'a=np.arange(8).reshape(2,2,2)：\n{a}')
print(f'\nb=np.arange(4).reshape(2,2)：\n{b}')
print (f'\nnp.matmul(a,b)=\n{np.matmul(a,b)}')
print(f"\na.dot(b)：\n{a.dot(b)}") 
print(f"\na@b：\n{a@b}") 


#------------
print('\n#(七)array常用方法')
a = np.array([(2, 3, 4), (5, 6, 7)])
print(f'若a=np.array([(2, 3, 4), (5, 6, 7)])：\n{a}')

b = a.sum() # a元素的總和
c = a.sum(axis=0) # 往下加 (沿著每個column計算-如科目總分)
d = a.sum(axis=1) # 往右加 (沿著每個row計算-如個人總分)
#print(f'a={a}')
print(f'\n則a元素的總和：b=a.sum()={b}')
print(f'col欄合計(如科目總分)：c=a.sum(axis=0)={c}')
print(f'row列合計(如個人總分)：d=a.sum(axis=1)={d}')
g = a.max() # a元素的最大值
h = a.min() # a元素的最小值
i = np.median(a) # a元素的中位數
j = np.mean(a) # a元素的平均值
k = np.std(a) # a元素的標準差
l = np.var(a) # a元素的變異數
print(f'a元素的最大值：g=a.max()={g}')
print(f'a元素的最小值：h=a.min()={h}')
print(f'a元素的中位數：i=np.median(a)={i}')
print(f'a元素的平均值：j=np.mean(a)={j}')
print(f'a元素的標準差1：k=np.std(a) ={k:6.3f}')
print(f'a元素的變異數：l=np.var(a)={l:6.3f}')
print(f'a元素的標準差2：k2=np.sqrt(l)={np.sqrt(l):6.3f}')







