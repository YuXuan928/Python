# =============================================================================
# 
# #繼承 1
# class Animal():      #定義父類別  
#     def __init__(self, name): #建構式前要 __init__( , )第1個參數要用self
#         self.name = name  #定義共用屬性         
#     def fly(self):        #定義共用方法 
#         print(self.name + "很會飛!")
#         
# class Bird(Animal):      #定義子類別  
#     def __init__(self, name):   #子類別建構式
#         self.name = "粉紅色" + name  #**覆寫父類別的建構式         
#     def sing(self):       #定義子類別的方法(增) 
#         print(self.name + "也愛唱歌!")        
# 
# pigeon = Animal("小白鴿")#以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
# pigeon.fly()  #小白鴿很會飛!
#       
# parrot = Bird("小鸚鵡")  #以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
# parrot.fly()  #粉紅色小鸚鵡很會飛!
# parrot.sing() #粉紅色小鸚鵡也愛唱歌!
# =============================================================================

# =============================================================================
# 🧪 練習題：動物家族 - 擴充建構子與方法
# ✅ 題目說明：
# 請你完成以下兩個類別：
# 🔸 父類別 Animal：
# 屬性：
# name：動物名稱
# color：顏色
# 方法：
# show_info()：輸出格式如下：
# 名稱：小白鴿；顏色：灰色
# 子類別 Bird（繼承 Animal）：
# 額外要求：
# 須使用 super() 呼叫父類別的 __init__
# 自動將 color 改為 "粉紅色"（不管傳進來的是什麼）
# 新增方法：
# sing()：輸出格式如下：
# 粉紅色的小鸚鵡正在唱歌！
# 📝 建立物件並測試：
# a1 = Animal("小白鴿", "灰色")
# a1.show_info()
# 
# b1 = Bird("小鸚鵡", "藍色")  # 不管這邊傳什麼 color，都要自動改為粉紅色
# b1.show_info()
# b1.sing()
# ✅ 預期輸出結果：
# 名稱：小白鴿；顏色：灰色
# 名稱：小鸚鵡；顏色：粉紅色
# 粉紅色的小鸚鵡正在唱歌！
# =============================================================================
# =============================================================================
# class Animal():
#
#     def __init__ (self , name , color):
#         self.name = name
#         self.color = color
#         
#     def show_info(self):    
#         print (f"名稱：{self.color} ; 顏色：{self.name}" )
#    
# class Bird (Animal):
#     def __init__ (self , name , color):
#         super().__init__(name , "粉紅色")     # 🔧 強制 color 為粉紅色
#         
#     def sing(self):
#         print(f"{self.color}的{self.name}正在唱歌!")
# 
# a1 = Animal ("小白鴿" , "灰色")
# a1.show_info()
# 
# b1 = Bird ("小鸚鵡" , "藍色")    # 傳入藍色，但實際 color 被設定為粉紅色
# b1.show_info()
# b1.sing()    
#     
# =============================================================================
# =============================================================================
# 🧪 練習題：動物行為大集合（繼承 + 多型 + 行為分類）
# ✅ 題目目標：
# 你要設計一個程式，有以下特色：
# 
# 🔸 Animal：父類別
# 屬性：name、color
# 
# 方法：show_info() 印出名稱與顏色
# 
# 🔸 子類別一：Bird
# 繼承 Animal
# 
# 增加 sing() 方法，會印出「[顏色]的[名稱]正在唱歌！」
# 
# 🔸 子類別二：Fish
# 繼承 Animal
# 
# 增加 swim() 方法，會印出「[顏色]的[名稱]正在游泳！」
# 
# 🔸 子類別三：Dog
# 繼承 Animal
# 
# 增加 bark() 方法，會印出「[顏色]的[名稱]正在汪汪叫！」
# b1 = Bird("小鸚鵡", "粉紅色")
# f1 = Fish("金魚", "金色")
# d1 = Dog("小黑", "黑色")
#  
# 名稱：小鸚鵡；顏色：粉紅色
# 粉紅色的小鸚鵡正在唱歌！
# 名稱：金魚；顏色：金色
# 金色的金魚正在游泳！
# 名稱：小黑；顏色：黑色
# 黑色的小黑正在汪汪叫！
# =============================================================================
class Animal():
    def __init__(self , name , color):
        self.name = name
        self.color = color
        
    def show_info(self):
        print(f"名稱:{self.name} : 顏色{self.color}")
        
class Bird(Animal):
    def __init__(self , name , color):
        super().__init__(name, color)
        
    def sing(self):
        print(f"{self.color}的{self.name}正在唱歌!")

class Fish(Animal):
    def __init__(self , name , color):
        super().__init__(name, color)
    
    def swim(self):
        print(f"{self.color}的{self.name}正在游泳!")
        
class Dog(Animal):
    def __init__(self , name , color):
        super().__init__(name, color)
   
    def bark(self):
        print(f"{self.color}的{self.name}正在汪汪叫!")

b1 = Bird("小鸚鵡", "粉紅色")
b1.show_info()
b1.sing()

f1 = Fish("金魚", "金色")
f1.show_info()
f1.swim()

d1 = Dog("小黑", "黑色")
d1.show_info()
d1.bark()       
        