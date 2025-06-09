#Abstraction
#import abc as ABC
from abc import ABC, abstractmethod #abc --- 抽象基底類別

#!!使用抽象類別，再配合運用資料繫結，使其達到多形的效果

class Operation(ABC):
    def __init__(self, x, y):   #父類別設屬性，子類別不設屬性
        self.x=x
        self.y=y
    @abstractmethod
    def Answer(self):
        pass

class CalAdd(Operation):
    #def __init__(self, x, y, z):
        #super().__init__(x, y)  #表x, y 的參數來自父類別
        #self.z=z  #子類別建構式第3參數z，指派子類別屬性self.z
        #上方三式在子類別的參數較多時，才需指出那幾個來自父類別，那些才是子類別的屬性
    def Answer(self):   #方法不使用參數x, y，使用父類別屬性
        return self.x+self.y

class CalSub(Operation):
    def Answer(self):   #方法不使用參數x, y，使用父類別屬性
        return self.x-self.y

class CalMul(Operation):
    def Answer(self):   #方法不使用參數x, y，使用父類別屬性
        return self.x*self.y

class CalDiv(Operation):
    def Answer(self):   #方法不使用參數x, y，使用父類別屬性
        return self.x/self.y    

#-------------
# 動態繫結的函式；顯示多型運算結果
def show_answers(operations: Operation):
    return operations.Answer()

#main
a=int(input('請輸入正數 a : '))
b=int(input('請輸入正數 b : '))

s=1
while s != 0 :
    s=int(input("\n請選擇  1)加法  2)減法  3)乘法  4)除法 < 結束：0 > "))
    if s == 0:
        continue
    elif s<0 or s>4:
        print('請輸入 0 - 4 的整數!')
        continue

    opr = [ CalAdd(a,b), CalSub(a,b), CalMul(a,b), CalDiv(a,b) ] #實作子類別
    
    op="+-*/"   #運算符號
    fm='0f' if s<4 else '3f'  #格式符號 除法使用小數3位
    print(f'{a} {op[s-1]} {b} = {opr[s-1].Answer():.{fm}}')

    
