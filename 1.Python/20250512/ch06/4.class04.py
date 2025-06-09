
#封裝
class Animal():      #定義類別  
    def __init__(self, name,age):            #建構式前要用 __init__( , )第1個參數要用self
        self.__name = name  #定義私用屬性     #*私用名稱前加上 __
        self.__age = age    #  "  "             "       "
    def __sing(self):       #定義私用方法     #*私用名稱前加上 __     
        print(self.__name + str(self.__age),end= "歲，很會唱歌，")  
    def talk(self):         #定義共用方法  self為必須
        self.__sing()       #使用私用方法  #*私用名稱前加上 __
        print("也會模仿人類說話!")  #會接self.__sing()的print(..,='..')之後(同列)顯示
        
bird = Animal("灰鸚鵡",2) #以 Animal 類別，建立一個名叫灰鸚鵡、2歲大的 bird物件
bird.talk()      #灰鸚鵡2歲，很會唱歌，也會模仿人類說話!

bird.__age = -1  #設定無效, 無法指派私用屬性
bird.talk()      #灰鸚鵡2歲，很會唱歌，也會模仿人類說話!
#bird.__sing()   #執行出現錯誤, 無法呼叫私用方法

# =============================================================================
# pratice more
# Q.建立一個 Person 類別，使用私有屬性 __password，並提供方法 check_password() 檢查密碼是否正確。
# 🎯 題目需求：
# 請你定義一個 Person 類別，具備以下功能：
# 
# 在建構時設定兩個屬性：
# 
# name（公有屬性）：使用者名稱
# 
# __password（私有屬性）：使用者密碼
# 
# 實作一個方法 check_password(input_password)：
# 
# 比對 __password 是否與輸入的密碼一致。
# 
# 一致就印出 登入成功!，否則印出 密碼錯誤!
# =============================================================================
class Person():
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        
    def check_password (self , input_password):
        if input_password == self.__password:     # 比對密碼
           print("登入成功!")
        else:
           print("密碼錯誤!")
          
# 建立使用者（帳號固定為「小明」，密碼為「abc123」）
p = Person("小明", "abc123")

# 提示使用者輸入密碼）
p_input = input("請輸入密碼:")    # 👉 登入成功!

# 驗證密碼是否正確）
p.check_password(p_input)     # 👉 密碼錯誤!


           