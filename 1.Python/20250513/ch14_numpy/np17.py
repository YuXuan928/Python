import numpy as np

#一維陣列的排序與遍歷(巡覽)
#choice(...,replace=False) #replace=False 表不重複
a = np.random.choice(50, size=10, replace=False) #在0<=x<=49 產生10個不重複的數
print('\na = np.random.choice(50, size=10, replace=False) #產生不重複資料') 
print('排序前的陣列 a：', a)
b=np.sort(a)
print('排序後的陣列 b=np.sort(a)：', b)
c=np.argsort(a)
print('排序後的索引 c=np.argsort(b)：', c)
#用索引到陣列取值
print('巡覽一維陣列 a：', a)


print('\n#一維陣列長度的三種表達方式') 
print('陣列 a 長度1：a.shape[0]=', a.shape[0])    
print('陣列 a 長度2：len(a)=', len(a))     
print('陣列 a 長度3：a.size=', a.size)   


