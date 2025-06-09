#基礎級 一般類別運用 (一個類別2個屬性4個方)
class Operation():
    def __init__(self, x, y):   #建構式
        self.x=x    #定義屬性 
        self.y=y    #定義屬性 
        
    def add(self):              #定義方法 add()
        return self.x+self.y
    def sub(self):              #定義方法 sub()
        return self.x-self.y
    def mul(self):              #定義方法 mul()
        return self.x*self.y
    def div(self):              #定義方法 div()
        return self.x/self.y

#main()
a=int(input('請輸入正數 a : '))
b=int(input('請輸入正數 b : '))
s=1
while s != 0 :
    s=int(input("\n請選擇  1)加法  2)減法  3)乘法  4)除法 < 結束：0 >"))
    if s == 0:
        continue
    opr=Operation(a, b)     #類別(Operation)實作 opr(物件)
    match s :
        case 1:
            msg=f'{a} + {b} = {opr.add()}'      #呼叫物件opr方法 add()
        case 2:
            msg=f'{a} - {b} = {opr.sub()}'      #呼叫物件opr方法 sub()
        case 3:
            msg=f'{a} * {b} = {opr.mul()}'      #呼叫物件opr方法 mul()
        case 4:
            msg=f'{a} / {b} = {opr.div():.3f}'  #呼叫物件opr方法 div()
        case _:
            msg='請輸入 1-4 的正整數!'
    print(msg)   
            