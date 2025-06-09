import numpy as np

#shape：取得陣列資訊
#list1=[ i for i in range(1, 25)]
#ary1=np.array(list1)
#上二式同下一式
ary1=np.arange(1,25)
np0=ary1.reshape(3,2,4)
print(f'\nnp0=\n{np0}')
#上段由指令產生同下段
np1 = np.array([[[1,2,3,4],[5,6,7,8]],
                [[9,10,11,12],[13,14,15,16]],
                [[17,18,19,20],[21,22,23,24]],
               ])
print(f"\nnp1=\n{np1}\n")

print(f"np1.shape={np1.shape}")    #(3, 2, 4) 
print(f"np1.shape[0]={np1.shape[0]} #维度")   #3 维度  #同np1.ndim
print(f"np1.shape[1]={np1.shape[1]} #row")   #2 row   #同np1.shape   
print(f"np1.shape[2]={np1.shape[2]} #col")   #4 col   #同np1.size  
print(f"np1.shape[-1]={np1.shape[-1]} #最後參數col")   #4 最後一個參數 col，

#一般來說，-1代表最後一個，所以shape[-1]在一、二、三維表示 col數

