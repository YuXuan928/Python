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