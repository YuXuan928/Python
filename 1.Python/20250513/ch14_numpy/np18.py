import numpy as np

#二維陣列排序與遍歷(巡覽)
a = np.random.randint(0,10,(3,5))   #產生0<=x<=9的 3x5陣列二維陣列
print('原陣列內容：')
print(a)
print('將每一直行進行排序：')
print(np.sort(a, axis=0))
print('將每一橫列進行排序：')
print(np.sort(a, axis=1))

print('巡覽二維陣列 a：')
for i in a:
    for j in i:
        print(j,end=' ')
    print()