import numpy as np

#改變陣列形狀
adata = np.arange(1,17)     #numpy.arange(start, stop, step) 起,止,間隔
print(f'1. adata={adata}')
bdata = adata.reshape(4,4)  #改變形狀成為 4x4
print(f'2. bdata=\n{bdata}\n')


print(f"adata.reshape(-1)={adata.reshape(-1)}")         #取得col 1-16
print(f"bdata.reshape(-1)={bdata.reshape(-1)}")         # 1-16
print(f"\nbdata.reshape(-1).shape={bdata.reshape(-1).shape}") #(16,)

print(f'bdata(不變)=\n{bdata}') #bdadta維持不變

cdata=bdata.reshape(-1,1)
print(f"\n3. cdata=bdata.reshape(-1,1)=\n{cdata}")   # 全部1-16, 分 col=1
print(f"\ncdata.shape={cdata.shape}\n")           #(16, 1)

ddata=bdata.reshape(-1,2)       #全部16，分col=2；同adata.reshape(8,2)
print(f"4. ddata=bdata.reshape(-1,2)=\n{ddata}",end="")  #  
print(f"\nddata.shape={ddata.shape}")           #(8, 2)

edata = adata.reshape(8,2)      #同bdata.reshape(-1,2)
print(f'\n5. edata = adata.reshape(8,2)=\n{edata}')
print(f"edata.shape={edata.shape}")   #(8, 2)
  