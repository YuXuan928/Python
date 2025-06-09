#from pkgutil import get_data
#from asyncore import loop
import random
#import statistics

class Student:

    global rng1, rng2, _sno, _tot, _avg 
    
    rng1, rng2 = 40, 101
    def __init__(self, sno, chi, eng, math):    # 建構式
        self.sno=sno
        self.chi=chi
        self.eng=eng
        self.math=math
        self._rank=0

    @property                           # 唯讀屬性
    def tot(self):
        return self.chi+self.eng+self.math

    @property                           # 唯讀屬性
    def avg(self):
        return self.tot/3
    
    def get_rank(self):
        return self._rank

    def set_rank(self,value):
        self._rank=value

    @property                            # 唯讀屬性
    def fail(self):
        return (1 if self.chi<60 else 0) + (1 if self.eng<60 else 0) + (1 if self.math<60 else 0)  

    def ToString(self) :        #自訂方法, 顯示個人成績相官資料
        print(f"{self.sno:-8} {self.chi:7}{self.eng:7}{self.math:7}{self.tot:7}{self.avg:7.1f}{self.rank:5}{self.fail:8}")
        
    
#-----------------

def GetScore() :    #產生3個亂數給國、英、數
    rng1, rng2 = 40, 100                    
    _chi = random.randint(rng1, rng2)       #**亂數範圍40 <= x <=100 
    _eng = random.randint(rng1, rng2)
    _math = random.randint(rng1, rng2)
    return _chi, _eng, _math                #回傳多值

def ListShow():     #顯示物件內容的方法
    print("  學  號    國 文  英 文  數 學   總 分  平 均  名次  不及格科目")
    print("  ======   =====  =====  =====  =====  =====  ====  ==========")
    for i in range(n):
        list[i].ToString()  #顯示物件內容
    print("  ------   -----  -----  -----  -----  -----  ----  ----------")
    print(f"         {chiavg:7.1f}{engavg:7.1f}{mathavg:7.1f}{totavg:7.1f}{avgavg:7.1f}")

def assign_ranks1(list):    #取得名次1
    totlist.sort()      #totlist排續(遞增)
    totlist.reverse()   #totlist排續(遞減)
    for i in range(n):                  #於totallist(降冪排序)中找原list[i].tot
        x=totlist.index(list[i].tot)    #同totlist.index(totlist0[i])   
        list[i].rank=x+1                #寫入名次屬性  
    
def assign_ranks2(list):    #取得名次2
    for i in range(len(list)):
        list[i].rank=list[i-1].rank if list[i].tot==list[i-1].tot else i+1
        #print(f'i={i}; list[i].rank')
        

#主程式
list=[]         #物件資料內容
totlist=[]      #遞減總分
no=113001       #學號
n=int(input("請輸入學生人數："))
n=20 if n>20 else n

for i in range(n):                  #類別實作
    data=GetScore()                 #取得學號及3科成績
    list.append(Student(no+i,data[0], data[1], data[2]))    #**實作各個學生
    totlist.append(list[i].tot)     #原始總分加入 totlist  (作排名用)


#求各科平均 To Get an average value of a property from a list of objects
chiavg = sum(p.chi for p in list)/len(list)
engavg = sum(p.eng for p in list)/len(list)
mathavg = sum(p.math for p in list)/len(list)
totavg = sum(p.tot for p in list)/len(list)
avgavg = sum(p.avg for p in list)/len(list)
#mean = statistics.mean((o.tot for o in list))  #**本式功能同上式totavg方法 import statistics
#print(f"mean={str(mean)}")

#取得名次1
#assign_ranks1(list)

#取得名次1
# 先按總分排序，然後分配排名
sorted_students = sorted(list, key=lambda s: s.tot, reverse=True)
assign_ranks2(sorted_students)


print("\n  顯示學生物件：原始資料")
ListShow()                          #顯示學生物件

#排序欄位選擇
while True:
    sel=input("選擇排序欄位[學號,國文,英文,數學...：1-8], [結束：0] ")
    if sel=="":
        continue
    s=ord(sel[0])
    #print(str(s))
    if s==48:
        print("程式結束!")
        break
    elif s<48 or s>56:  # s<0 or s>56
        print("請輸入0-8的數字!")
        continue

    elif s==49 :    #1
        list.sort(key=lambda x: x.sno, reverse=False)    #以學號遞增排序
        print("\n  顯示學生物件：學號遞增")               
    elif s==50 :    #2    
        list.sort(key=lambda x: x.chi, reverse=True)    #以國文遞減排序
        print("\n  顯示學生物件：國文遞減")
    elif s==51 :    #3
        list.sort(key=lambda x: x.eng, reverse=True)    #以英文遞減排序
        print("\n  顯示學生物件：英文遞減")
    elif s==52 :    #4
        list.sort(key=lambda x: x.math, reverse=True)    #以數學遞減排序
        print("\n  顯示學生物件：數學遞減")
    elif s==53 :    #5
        list.sort(key=lambda x: x.tot, reverse=True)    #以總分遞減排序
        print("\n  顯示學生物件：總分遞減")
    elif s==54 :    #6
        list.sort(key=lambda x: x.avg, reverse=True)    #以個人平均遞減排序
        print("\n  顯示學生物件：個人平均遞減")
    elif s==55 :    #7
        list.sort(key=lambda x: x.rank, reverse=False)    #以名次遞增排序
        print("\n  顯示學生物件：名次遞增")  
    else : #s==56 :    #8
        list.sort(key=lambda x: x.fail, reverse=False)    #以不及格科目遞增排序
        print("\n  顯示學生物件：不及格科目遞增")       

    ListShow()          #顯示不同排序後的學生物件
