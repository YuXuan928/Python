# -*- coding: utf-8 -*-
"""
Spyder Editor
felix 2024/04/22
"""
import time as tm
#import datetime as dt
import calendar
from datetime import datetime  as dt_tm #使用本式，可以不需要datetime.datetime
from datetime import timedelta #日期差或日期操作使用
#import datetime



print('#1.將localtime()使用指定字串格式化顯示')
print('strftime("%Y-%m-%d %H:%M:%S",tm.localtime()):',end=' ')
print (tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime()))

print('strftime("%a %b %d %H:%M:%S %Y",time.localtime()):',end=' ')
print (tm.strftime("%a %b %d %H:%M:%S %Y", tm.localtime()))
#a:星期、b:月份、d:日

cal = calendar.month(2025, 5)
print ("\n以下輸出2025年5月份的日曆:")
print (cal)
#-------

print('\n#2.指定時間數據(轉日期型態)')
print('dt_tm(2021, 10, 15, 17, 37, 7, 490703)：', end='')
print(dt_tm(2021, 10, 15, 17, 37, 7, 490703))
print('datetime(2021, 10, 15, 9, 37, 43, 823644)：', end='')
print(dt_tm(2021, 10, 15, 9, 37, 43, 823644))
#-------

print('\n#3.時間->時戳的轉換：')
print('#取得現在的時間：')
tt = dt_tm.today() # 現在的時間，計到微秒
print(f'(1)datetime.today()： {dt_tm.today()}')
tn = dt_tm.now()
print(f'(2)datetime.now()： {dt_tm.now()}')
print(f'(3)tn.isoformat()： {dt_tm.now().isoformat()}')  # isoformat語法印出的結果會用「T」來分隔日期和時間
print(f'(4)datetime.utcnow()：{dt_tm.utcnow()}', end=" #UTC時間\n") # UTC標準時間（台灣是+8）

print('\n#時間的轉換：')
print(f'tn=datetime.now()：{tn}')
print(f'時間->時戳 ts=tn.timestamp()：{tn.timestamp()}', end='')
ts = tn.timestamp()
print('\n時戳->時間 datetime.fromtimestamp(ts)：', end='')
print(dt_tm.fromtimestamp(ts))   #tn

print('時間->ISO時間 datetime.now().isoformat()：', end='')
tiso = tn.isoformat() # 取得ISO時間
print(tiso)
print('時戳->utc時間  datetime.utcfromtimestamp(ts)：', end='')
print(dt_tm.utcfromtimestamp(ts)) # 將時間戳轉回UTC+0格式
print('ISO時間-> 時間 datetime.fromisoformat(tiso)：', end='')
print(dt_tm.fromisoformat(tiso)) # 將ISO time轉回 datetime格式
#-------

print('\n#4時間差.timedelta') #下方範例是參數的時間總和
td = timedelta(weeks=1, days=30, hours=2, minutes=40)
print('timedelta(weeks=1, days=30, hours=2, minutes=40)',end='：')
print(td)  # 37 days, 2:40:00

dt1 = dt_tm(2021, 10, 15, 11, 18, 0)
dt2 = dt_tm(2021, 10, 14, 9, 11, 0)
print(f'dt1:{dt1} - dt2:{dt2}',end='：')
print(dt1 - dt2) # 1 day, 2:07:00

# 將兩個時間間隔相減，可以得到另一個 timedelta 對象：
td1 = timedelta(days=25) # 25 days
td2 = timedelta(weeks=1) # 1 week
print('td1(day_25) - td2(weeks_1)', end='：')
print(td1 - td2) # 18 days, 0:00:00
#-------


print('\n#5.計算未來某一天的日期')

#now=dt_tm(2024, 12, 15)
now = dt_tm.now()
print('現在時間 now = datetime.now()：{now}')

future_date1 = now + timedelta(days=1)    #current date and time
print('未來 1天 datetime.now() + timedelta(days=7)：{future_date1}')
future_date7 = now + timedelta(days=7)
print('未來 7天 datetime.now() + timedelta(days=7)：{future_date7}')

print('\n#6.datetime轉文字的年月日：')
print('  #6.1由 now() 的屬性取得年、月、日：')
print('  now()的年now().year, 月now().month, 日now().day ', end='：')
print(now.year, end=', ')
print(now.month, end=', ')
print(now.day)

print("  #6.2由 now.strftime()'%Y'、'%m'、'%d': 的屬性取得年、月、日：")
#year = now.strftime("%Y")
#print(f"year:" year, end='：')
print(f"  年 now.strftime('%Y'): {now.strftime('%Y')}")
print(f"  月 now.strftime('%m'): {now.strftime('%m')}")
print(f"  日 now.strftime('%d'): {now.strftime('%d')}")

week='一二三四五六日'
print("\n#如果week='一二三四五六日', 則　星期{week[now.weekday()]}", end="：")
print(f'星期{week[now.weekday()]}') #星期一是0，星期日是6


print('\n#7.時間轉字串格式-星期、月份、日期、時間')
#dt = datetime.now()  
print('now.strftime((%Y-%m-%d %H:%M:%S %f): ' , now.strftime( '%Y-%m-%d %H:%M:%S %f' )) 
print('now.strftime((%Y-%m-%d %H:%M:%S %p): ' , now.strftime( '%y-%m-%d %I:%M:%S %p' ))  
print('\n#星期、月份的表達')
print(f"星期(簡)now.strftime('%a'): {now.strftime('%a')}")  
print(f"星期英文now.strftime('%A'): {now.strftime('%A')}") 

print(f"月份(簡)now.strftime('%b'): {now.strftime('%b')}")  
print(f"月份英文now.strftime('%B'): {now.strftime('%B')}")  
print('\n(7.1)日期時間、日期、時間')
print(f"日期時間now.strftime('%c'): {now.strftime('%c')}")  
print(f"單純日期now.strftime('%x'): {now.strftime('%x')}") 
print(f"單純時間now.strftime('%X'): {now.strftime('%X')}") 
print('\n(7.2)日期時間、日期、時間')
print(f"日期時間2 now.strftime('%Y-%m-%d, %H:%M:%S'): {now.strftime('%Y-%m-%d, %H:%M:%S')}") 
print(f"單純日期2 now.strftime('%Y-%m-%d'): {now.strftime('%Y-%m-%d')}") 
print(f"單純時間2 now.strftime('%H:%M:%S'): {now.strftime('%H:%M:%S')}") 

print('\n#(7.3)週與星期、月份的表達')
x=now.strftime('%w')    #string
x=int(x)+1
print(f"今天是這周的第x天now.strftime('%w')+1:{x} 天") 
print(f"今天是這個月的第x天now.strftime('%d'): x={now.strftime('%d')}天") 
print(f"今天是今年的第x天now.strftime('%j'): x={now.strftime('%j')}天") 
print(f"本周是今年的第x周now.strftime('%U'): x={now.strftime('%U')}週")
#strftime('%U') #星期天為星期的開始
print('\n#(7.4)週與星期、月份的表達')
y=(now.weekday()+2)%6   #星期日為0，
print(f"今天是這周的第x天 (now.weekday()+2)%6:{y} 天") 
dlt = now - dt_tm(now.year, 1, 1)
print(f"今天是這個月的第x天 now.days  : x={now.day}天") 
md=dlt.days+1
print(f"今天是今年的第x天 dlt=(now-元旦+1);dlt.days+1: x={dlt.days+1}天") 
print(f"本周是今年的第x周 md=dlt.days+1 : {(md)//7}週")

print(f'\n#8.傳回文字形態：time.ctime()={tm.ctime()}')   #current date and time
now1=dt_tm.now()
print(f'現在時間：now1=datetime.now()={now1.ctime()}')
now7 = (now1+timedelta(days=7))    #7天後 date and time
print(f'未來7天：now1+timedelta(days=7)={now7.ctime()}')


print('\n#9.日期的文字型態 轉 日期型態')
print('#datetime.strptime 日期的文字型態 轉 日期型態')
#dts = str(input("(20200710):"))
dts1='20200710'
dt1 = dt_tm.strptime(dts1,"%Y%m%d")
print(f"datetime.strptime('{dts1}','%Y%m%d')：",dt1) #2020-07-10 00:00:00
    
dts2 = dts1[:4]+"0101"  #取sdts1的前4碼 '2020' + '0101'
dt2 = dt_tm.strptime(dts2,"%Y%m%d")
print(f"datetime.strptime('{dts2}','%Y%m%d')：",dt2) #20200710-20200101=>int((dt1-dt2).days)+1=192
print(f"{dts1}-{dts2}=>int((dt1-dt2).days)+1={int((dt1-dt2).days)+1}")
#20200710-20200101=>int((dt1-dt2).days)+1=192

str_time = "2023年1月2日12點25分30秒"
time = dt_tm.strptime(str_time, "%Y年%m月%d日%H點%M分%S秒")
print(f"datetime.strptime({time}, '%Y年%m月%d日%H點%M分%S秒'") #2023-01-02 12:25:30



'''
%U 一年中的星期數（00-53）星期天為星期的開始
%w 星期（0-6），星期天為星期的開始
%W 一年中的星期數（00-53）星期一為星期的開始
weekday()	回傳一星期中的第幾天，星期一為 0

ISO 時間更適合跨時區、跨系統使用，避免因本地時區不同而出現錯誤。
UTC 與 GMT 的差異
UTC（協調世界時）：國際標準時間，精度更高
GMT（格林威治標準時間）：早期的時間標準，主要用於日常生活與歷史記錄
現在多數技術系統使用 UTC 作為標準時間，而 GMT 常見於新聞或日常溝通。
'''