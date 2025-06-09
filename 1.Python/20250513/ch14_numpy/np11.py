import numpy as np

#多維陣列取值
na = np.arange(1, 17).reshape(4, 4)
print(na)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
'''
print(f"\nna[2, 3]={na[2, 3]}")		        #12              #index[2,3] 第3row(2+1)，第4col(3+1)
print(f"\nna[1, 1:3]={na[1, 1:3]}")	        #[6,7]           #index[1, (1,2)]第2row，第2,3col
print(f"\nna[1:3, 2]={na[1:3, 2]}")	        #[7,11]          #index[(1,2),2]第2,3row，第3col
print(f"\nna[1:3, 1:3]=\n{na[1:3, 1:3]}")   #[[6,7],[10,11]] #index[(1,2),(1,2)]第2,3row，第2,3col  
print(f"\nna[::2, ::2]=\n{na[::2, ::2]}")   #[[1,3],[9,11]]  #index row:0隔2, col 0隔2
print(f"\nna[:, 2]={na[:, 2]}")		        #[3,7,11,15]     #col=2的全部
print(f"\nna[1, :]={na[1, :]}")		        #[5,6,7,8]       #row=1的全部
print(f"\nna[:, :]=\n{na[:, :]}")		    #矩陣全部