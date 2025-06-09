import random

#產生三科成績的亂數方法在類別內
class Student:
    __start_id = 114001     #類別變數 私有變數
    rng1, rng2 = 40, 100    #類別變數
    def __init__(self, id):    # 建構式
        self.sno=self.__start_id+id
        self.chi, self.eng, self.math = self.GetScore()  # 呼叫類別方法取得成績
        self._rank=0

    @property                           # 唯讀屬性
    def tot(self):
        return self.chi+self.eng+self.math

    @property                           # 唯讀屬性
    def avg(self):
        return self.tot/3
    
    '''
    def get_rank(self):
        return self._rank

    def set_rank(self,value):
        self._rank=value
    '''
    #較方便的屬性寫法
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    #-----------

    @property                            # 唯讀屬性
    def fail(self):
        return (1 if self.chi<60 else 0) + (1 if self.eng<60 else 0) + (1 if self.math<60 else 0)  

    def ToString(self) :        #自訂方法, 顯示個人成績相官資料
        print(f"{self.sno:-8} {self.chi:7}{self.eng:7}{self.math:7}{self.tot:7}{self.avg:7.1f}{self.rank:5}{self.fail:8}")
        
    def GetScore(self):  # 產生3個亂數給國、英、數
        _chi = random.randint(Student.rng1, Student.rng2)
        _eng = random.randint(Student.rng1, Student.rng2)
        _math = random.randint(Student.rng1, Student.rng2)
        return _chi, _eng, _math  # 回傳多值
    
#-----------------

def ListShow(list):     #顯示物件內容的方法
    print("  學  號    國 文  英 文  數 學   總 分  平 均  名次  不及格科目")
    print("  ======   =====  =====  =====  =====  =====  ====  ==========")
    for i in range(n):
        list[i].ToString()  #顯示物件內容
    print("  ------   -----  -----  -----  -----  -----  ----  ----------")
    print(f"         {chiavg:7.1f}{engavg:7.1f}{mathavg:7.1f}{totavg:7.1f}{avgavg:7.1f}")

def assign_ranks1(list):    #取得名次1
    totlist.sort()          #totlist排續(遞增)
    totlist.reverse()       #totlist排續(遞減)
    for i in range(n):      #於totallist(降冪排序)中找原list[i].tot
        x=totlist.index(list[i].tot)      
        list[i].rank=x+1    #寫入名次屬性  
    
def assign_ranks2(list):    #取得名次2
    for i in range(len(list)):
        list[i].rank=list[i-1].rank if list[i].tot==list[i-1].tot else i+1
        #!本作法list需先對list.tot作降覓排序


#主程式
#list=[]         #物件資料內容
totlist=[]      #遞減總分
no=113001       #學號
n=int(input("請輸入學生人數："))
n=20 if n>20 else n

stus = [Student(i) for i in range(n)]    #產生多個的stus
totlist=[stus[i].tot for i in range(n)]  

for i in range(n):
    print(stus[i].sno, stus[i].chi, stus[i].eng, stus[i].math, stus[i].tot)


#求各科平均 To Get an average value of a property from a list of objects
chiavg = sum(p.chi for p in stus)/len(stus)
engavg = sum(p.eng for p in stus)/len(stus)
mathavg = sum(p.math for p in stus)/len(stus)
totavg = sum(p.tot for p in stus)/len(stus)
avgavg = sum(p.avg for p in stus)/len(stus)


#取得名次1
#assign_ranks1(stus)

#取得名次1
# 先按總分排序，然後分配排名
sorted_students = sorted(stus, key=lambda s: s.tot, reverse=True)
assign_ranks2(sorted_students)


print("\n  顯示學生物件：原始資料")
ListShow(stus)          #顯示學生物件

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
        stus.sort(key=lambda x: x.sno, reverse=False)    #以學號遞增排序
        print("\n  顯示學生物件：學號遞增")               
    elif s==50 :    #2    
        stus.sort(key=lambda x: x.chi, reverse=True)    #以國文遞減排序
        print("\n  顯示學生物件：國文遞減")
    elif s==51 :    #3
        stus.sort(key=lambda x: x.eng, reverse=True)    #以英文遞減排序
        print("\n  顯示學生物件：英文遞減")
    elif s==52 :    #4
        stus.sort(key=lambda x: x.math, reverse=True)    #以數學遞減排序
        print("\n  顯示學生物件：數學遞減")
    elif s==53 :    #5
        stus.sort(key=lambda x: x.tot, reverse=True)    #以總分遞減排序
        print("\n  顯示學生物件：總分遞減")
    elif s==54 :    #6
        stus.sort(key=lambda x: x.avg, reverse=True)    #以個人平均遞減排序
        print("\n  顯示學生物件：個人平均遞減")
    elif s==55 :    #7
        stus.sort(key=lambda x: x.rank, reverse=False)    #以名次遞增排序
        print("\n  顯示學生物件：名次遞增")  
    else : #s==56 :    #8
        stus.sort(key=lambda x: x.fail, reverse=False)    #以不及格科目遞增排序
        print("\n  顯示學生物件：不及格科目遞增")       

    ListShow(stus)  #顯示不同排序後的學生物件
