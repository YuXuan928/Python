# =============================================================================
# #繼承 2 (父子類別相同的屬性與方法)
# class Animal():      #定義父類別  
#     def __init__(self,name):    #建構式前要用 __init__( , )第1個參數要用self
#         self.name = name  #定義共用屬性         
#     def fly(self):        #定義共用方法 
#         print(self.name + "很會飛!")
#         
# class Bird(Animal):       #定義子類別  
#     def __init__(self,name,age):
#         super().__init__(name) #執行父類別的 __init__()方法 #**需用 super().__init__(name)
#         self.age = age    #定義子類別共用屬性 
#     def fly(self):        #定義子類別共用方法         
#         print(str(self.age),end="歲") 
#         super().fly()     #執行父類別的 fly方法     #**需用 super().
# 
# pigeon = Animal("小白鴿") #以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
# pigeon.fly()  #小白鴿很會飛!
#       
# parrot = Bird("小鸚鵡",2) #以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
# parrot.fly()             #2歲小鸚鵡很會飛!
# =============================================================================
# 🧪 練習題：動物樂園（方法覆寫 + 多型 + super()）
# ✅ 題目說明：
# 請你完成以下類別架構：
# 🔹 父類別 Animal
# 屬性：name
# 方法：
# move()：印出「[name] 正在移動！」
# 🔹 子類別們（都繼承 Animal）：
# Bird
# 增加屬性：age
# 覆寫 move() 方法：
# 先印出「[age] 歲」，再呼叫父類別的 move()。
# 額外印出：「它用翅膀飛翔。」
# 
# Fish
# 覆寫 move() 方法：
# 先印「[name] 是水中動物，」
# 再呼叫父類別 move()。
# 額外印：「它在水中游泳。」
# 
# Dog
# 覆寫 move() 方法：
# 印出：「[name] 用四腳在地上跑！」
# 📝 建立以下物件並放進列表：
# b1 = Bird("小鸚鵡", 2)
# f1 = Fish("金魚")
# d1 = Dog("小黑")
# 然後使用 for 迴圈依序呼叫 .move()：
# animals = [b1, f1, d1]
# for a in animals:
#     a.move()
# ✅ 預期輸出結果：
# 2 歲
# 小鸚鵡 正在移動！
# 它用翅膀飛翔。
# 金魚 是水中動物，
# 金魚 正在移動！
# 它在水中游泳。
# 小黑 用四腳在地上跑！
# =============================================================================
class Animal():
    def __init__(self,name):
        self.name = name
        
    def move(self):
        print (f"{self.name} 正在移動!")
        
class Bird(Animal):
    def __init__(self , name , age):
        super().__init__(name)     # ✅ 呼叫父類別 __init__ 設定 name
        self.age = age             # ✅ 自己的屬性 
         
    def move (self):
        print(f"{self.age} 歲")    # ✅ 顯示年齡
        super().move()             # ✅ 呼叫 Animal 的 move()
        print("牠用翅膀飛翔")       # ✅ 額外行為
        
class Fish(Animal):
    def __init__(self , name):
        super().__init__(name)
        
    def move (self):
        print(f"{self.name}是水中動物!")
        super().move()
        print("牠在水中游泳!")
        
class Dog(Animal):
    def __init__(self , name):
        super().__init__(name)

    def move (self):
        print(f"{self.name}用四隻腳在地上跑!")
        
        
b1 = Bird ("小鸚鵡" , 2)
f1 = Fish ("金魚")
d1 = Dog ("小黑")


animals = [b1 ,f1 ,d1 ]
for a in animals:
    a.move()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        