
class Animal():      #定義類別
    name = "小鳥"    #定義屬性
    def sing(self):  #定義方法
        print("很會唱歌!")     
        
bird = Animal()  #以 Animal 類別，建立一個名叫小鳥的 bird物件
print(bird.name) #小鳥
bird.sing()      #很會唱歌!

#pratice
class shape():
    ex = "正方形"
    def corners(self):
        print("有四個角")
square = shape()
print(shape.ex)
square.corners()    

#pratice
# =============================================================================
# 🔧 題目需求：
# 請你完成一個 Student 類別，具備以下條件：
# 
# 類別屬性：
# 
# school：預設為 "北一女中"
# 
# 物件屬性（在建構時給）：
# 
# name：學生姓名
# 
# score：分數
# 
# 加入一個方法 show_info()，印出：
# 
# 複製
# 編輯
# 學生：小美；分數：95；學校：北一女中
# 🔸 請試著完成這個類別，提示如下：
# python
# 複製
# 編輯
# class Student:
#     school = "北一女中"  # 類別屬性
# 
#     def __init__(self, name, score):
#         self.name = _______  # 物件屬性
#         self.score = _______
# 
#     def show_info(self):
#         print(f"學生：{self.name}；分數：{self.score}；學校：{______}")
# ✅ 加分挑戰題（可選）：
# 建立兩個學生物件：s1 = Student("小美", 95)、s2 = Student("小君", 88)
# 
# 改變 s2 的學校為 "建中"（但不要改到其他學生）
# 
# 分別印出兩個學生的資訊，觀察差異！    
# =============================================================================

class Student:
    school = "北一女中"
    def __init__(self, name, score):
        self .name = name
        self .score = score
    def show_info(self):
        print(f'學生:{self.name} ; 分數:{self.score} ; 學校:{self.school}')
        
s1 = Student("小美" , 95)        
s2 = Student("小君" , 88)

s2.school = "建中一中"

s1.show_info()   # 學生：小美；分數：95；學校：北一女中
s2.show_info()   # 學生：小君；分數：88；學校：建中


        