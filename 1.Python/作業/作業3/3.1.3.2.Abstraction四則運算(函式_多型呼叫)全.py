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
def show_answers(operations: list[Operation]):
    i=0
    sym='+-*/'
    for op in operations:
        fm='0' if i<3 else '3'  #格式符號 除法使用小數3位
        print(f'{a} {sym[i]} {b} = {op.Answer():.{fm}f}')
        i+=1


a=int(input('請輸入正數 a : '))
b=int(input('請輸入正數 b : '))
opr = [ CalAdd(a,b), CalSub(a,b), CalMul(a,b), CalDiv(a,b) ] #實作子類別
show_answers(opr) #顯示結果
    

    
