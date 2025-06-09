from mypackage.Hello import sayHello
from mypackage.Hello import  IsLeap   #自定閏年判斷 IsLeap 在 Hello 內
from mypackage.Isleap import  MyIsLeap  #自定閏年判斷 Isleap讀立一個 py

sayHello()
print(IsLeap(2024))     #參數2024 
print(MyIsLeap(2020))
print(MyIsLeap('西元2020'))
print(IsLeap('西元2016'))