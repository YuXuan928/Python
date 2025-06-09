# =============================================================================
# class Animal():      #定義類別  
#     def __init__(self, name):   #建構式 必須使用__init__、參數 self
#         self.name = name        #定義屬性   
#     def sing(self):             #定義方法  self為必須      
#         print(self.name + "，很會唱歌!")     
#         
# bird = Animal("鸚鵡")  #以 Animal 類別，建立一個名叫鸚鵡的 bird物件
# print(bird.name) #鸚鵡
# bird.sing()      #鸚鵡，很會唱歌!
# =============================================================================

# =============================================================================
# 💡 延伸練習（自訂更多動物）
# 你可以再試幾個不同的物件，例如：
# 
# python
# 複製
# 編輯
# a1 = Animal("八哥")
# a2 = Animal("畫眉")
# 
# a1.sing()   # 八哥，很會唱歌!
# a2.sing()   # 畫眉，很會唱歌!
# =============================================================================
class Animal():
    def __init__(self,name,song):
        self.name = name
        self.song = song
    def sing(self):
        print(f"{self.name}會唱 : {self.song}")

a1 = Animal ("八哥","祝你生日快樂")
a2 = Animal ("畫眉","王老先生有塊地")        

a1.sing()
a2.sing()        


