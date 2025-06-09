# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:27:18 2024

@author: Felix
"""
import numpy as np

a=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(f"a=\n{a}")
print(f"\nb=\n{b}")

print(f"\n(1)multiply(a,b) #對應位置的乘積：\n{np.multiply(a,b)}")
print(f"\n(2)a*b #元素乘積(同上)：\n{a*b}")
print(f"\n(3)np.matmul(a, b) #矩陣乘法，列*行後相加：\n{np.matmul(a, b)}") 
print(f"\n(4)a@b #矩陣乘法，上式簡寫：\n{a@b}") 
print(f"\n(5)a.dot(b)點積：\n{a.dot(b)}") 



#內積：
print(f"\na=\n{a}")
print(f"\nb.T=\n{b.T}")
print(f"\n(6)a@b.T #內積：\n{a@b.T}") 
print(f"\n(7)np.inner(a, b) #內積：\n{np.inner(a, b)}") 


#外積：
'''
at=np.arange(1,10)
bt=10*at
print(at)
print(bt)
'''
print(f"\na=\n{a}")
print(f"\nb=\n{b}")
print(f"\n(8)np.outer(a, b) #外積：\n{np.outer(a, b)}") 




