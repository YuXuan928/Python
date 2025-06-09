#Abstraction
#import abc as ABC
from abc import ABC, abstractmethod #abc --- 抽象基底類別
#4個子類別繼承父類別，屬性在父類別(子類別不使用建構子，沒有supper、self屬性區分)


class Operation(ABC):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    @abstractmethod
    def Answer(self):
        pass

class CalAdd(Operation):
    #def __init__(self, x, y, z):
    #    super().__init__(x, y)  #表x, y 的參數來自父類別
    #    self.z=z  #子類別建構式第3參數z，指派子類別屬性self.z
    #上方三式在子類別的參數較多時，才需指出那幾個來自父類別，那些才是子類別的屬性
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

a=int(input('請輸入正數 x : '))
b=int(input('請輸入正數 y : '))
s=1
while s != 0 :
    s=int(input("\n請選擇  1)加法  2)減法  3)乘法  4)除法 < 結束：0 > "))
    if s == 0:
        continue
    op="+-*/"   #運算符號
    match s :
        case 1:
            opr=CalAdd(a, b)
        case 2:
            opr=CalSub(a, b)
        case 3:
            opr=CalMul(a, b)
        case 4:
            opr=CalDiv(a, b)
        case _:
            msg='請輸入 1-4 的正整數!'
    if 0 < s < 5:
        msg=f'{a} {op[s-1]} {b} = {opr.Answer()}'
    print(msg)            
