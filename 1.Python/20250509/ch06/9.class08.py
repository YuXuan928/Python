#多重繼承
class Father():         #定義父類別         
    def say(self):      #定義共用方法 
        print("明天會更好!")
        
class Mother():         #定義父類別  
    def say(self):      #定義共用方法 
        print("包容、尊重!")
        
class Child(Father,Mother): #定義子類別  
    pass    #P pass 不能省略
        
child = Child() #建立 child 物件
child.say()     #明天會更好! 

'''
child.say()會優先找Child的方法，如果找不到再找Father()、Mother()
'''