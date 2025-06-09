import numpy as np

#讀取檔案取值
a = np.genfromtxt('scores.csv', delimiter=',', skip_header=1)

print(f"檔案內容\n{a}")
print(f"a.shape={a.shape}")