import numpy as np

#a = np.random.randint(100,size=50)
a1=[ 6, 8, 10, 14, 12, 7, 5, 15, 2, 4]     #list 偶數個
#a1=[ 6, 8, 10, 14, 7, 5, 15, 2, 4]        #list 奇數個
a=np.array(a1);             #list 轉 array
a=np.sort(a)
print('陣列的內容：', a)

print('\n#使用numpy函式：')
print('1.平均數：np.mean(a)=',np.mean(a))
print('2.標準差：np.std(a)=', np.std(a))
print('3.變異數：np.var(a)=', np.var(a))
print('4.中位數：np.median(a)=', np.median(a))
print('5.百分比值Q3：np.percentile(a, 75)=', np.percentile(a, 75))
print('6.最大最小差值：np.ptp(a)=', np.ptp(a))



