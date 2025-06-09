import numpy as np
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('1. a=np.arange(1,10).reshape(3,3)：\n', a)
print('\n2. b=np.arange(10,19).reshape(3,3)：\n', b)
print('\n3. a 陣列元素都加值 1 => a + 1：\n', a + 1)
print('\n4. a 陣列元素都平方 => a ** 2：\n', a ** 2)
print('\n5. a 陣列元素加判斷 => a < 5：\n', a < 5)
print('\n6. a 陣列取出第一個row都加 1 => a[0,:] + 1：\n', a[0,:] + 1)
print('\n7. a 陣列取出第一個col都加 1 => a[:,0] + 1：\n', a[:,0] + 1)
print('\n8. a, b 陣列對應元素相加 => a + b：\n', a + b)
print('\n9. a, b 陣列對應元素相乘 => a * b：\n', a * b)
print('\n10. a, b 矩陣乘法1 => np.matmul(a,b)：\n', np.matmul(a,b)) #同a @ b(簡寫版)
print('\n11. a, b 矩陣乘法2 => np.dot(a,b)：\n', np.dot(a,b))

'''
#matmul與 dot 都是矩陣乘法 (Matrix Multiplication)，兩者非常類似，其相同及不同點如下：
(1).如果2個都是二維陣列的話，matmul與 dot 相同。
(2).在 matmul 中，多維的矩陣，將前 n-2 維視為後2维的元素後，進行乘法運算。
(3).matmul 不允許矩陣與純量相乘。
在 Python 3.5版本之後提供@做為矩陣相乘運算子，提供更簡潔的語法。
'''