import numpy as np

#產生隨機資料
print('1.np.random.rand(2,3)：產生2x3 0~1之間的隨機浮點數\n',
      np.random.rand(2,3))
print('2.np.random.randn(2,3)：產生2x3常態分佈的隨機浮點數\n',
      np.random.randn(2,3))
print('3.np.random.randint(5)：產生0~4(不含5)隨機整數\n',
      np.random.randint(5))
print('4.np.random.randint(2,5,[5])：產生2~4(不含5)5個隨機整數\n',
      np.random.randint(2,5,[5]))
print('5.產生3個 0~1之間的隨機浮點數')
print(f'5.1.np.random.random(3)\t\t\t={np.random.random(3)}')
print(f'5.2.np.random.random_sample(3)  ={np.random.random_sample(3)}')
print(f'5.3.np.random.sample(3)\t\t\t={np.random.sample(3)}')
print(f"6.np.random.choice(5,[2,3])：產生0~4(不含5)2x3的隨機整數\n{np.random.choice(5,[2,3])}")
print(f"7.np.random.choice(43,6,replace=False)：產生0~42(不含43)6個不重複的隨機整數\n{np.random.choice(43,6,replace=False)}")
