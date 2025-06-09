#Abstraction
#import abc as ABC
from abc import ABC, abstractmethod

class Operation(ABC):
        def __init__(self, x, y):
            self.x=x
            self.y=y
        @abstractmethod
        def Answer(delf):
            pass

class CalAdd(Operation):
    def Answer(self):
        return self.x+self.y

class CalSub(Operation):
    def Answer(self):
        return self.x-self.y

class CalMul(Operation):
    def Answer(self):
        return self.x*self.y

class CalDiv(Operation):
    def Answer(self):
        return self.x/self.y    

#-------------

x1=int(input('請輸入正數 x : '))
y1=int(input('請輸入正數 y : '))
s=1
while s != 0 :
    s=int(input("\n請選擇  1)加法  2)減法  3)乘法  4)除法 < 結束：0 >"))
    if s == 0:
        continue
    match s :
        case 1:
            add=CalAdd(x1, y1)
            print(f'{x1} + {y1} = {add.Answer()}')
        case 2:
            sub=CalSub(x1, y1)
            print(f'{x1} - {y1} = {sub.Answer()}')
        case 3:
            mul=CalMul(x1, y1)
            print(f'{x1} * {y1} = {mul.Answer()}')
        case 4:
            div=CalDiv(x1, y1)
            print(f'{x1} / {y1} = {div.Answer():.3f}')
        case _:
            print('請輸入 1-4 的正整數!')
