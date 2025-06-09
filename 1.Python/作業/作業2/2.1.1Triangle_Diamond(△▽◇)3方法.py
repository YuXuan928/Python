
#使用3個函數處理3個形狀選項

def Chart1(n):     #正向三角形
    global s, t, str
    for i in range(1, n+1):             #由上而下(列數)
        str+='　'*(n-i);                #每列加空白
        #for j in range(1, i + 1):      #由左而右顯示(★個數遞增)
        #    str += s + t
        str+=(s + t)*i                  #功能同上方迴圈
        str += "\n"                     #跳(換)下2列(中間空一列
    return str


def Chart2(n):     #倒立三角形
    global s, t, str
    for i in range(1, n + 1):
        str+='　'*(i-1);                 #每列加空白
        #for j in range(1, n + 2 - i):   #由左而右顯示(★個數遞減)
        #    str += s + t                 若要用遞減方式表示需要一個固定數來做運算
        str+=(s + t)*(n + 1 - i)         #!!以本式替代商方迴圈           
        str += "\n"
    return str


def Chart3(n):     #菱形
    global s, t, str
    i=1
    for z in range(1, 2 * n):           #i 跑 2*-1 圈的 一組模式
        str+='　'*(n-i);                #每列加空白
        #for j in range(1, i + 1):      #由左而右顯示(★個數遞減)
        #    str += s + t
        str+=(s + t)*i                  #!!以本式替代商方迴圈  
        str += "\n";
        i = i+1 if (z < n) else i - 1   #上半 i+1 (遞增)、下半 i-1 (遞減) 
    return str



while (True):
    #畫星星
    s=input("請選擇, (1)正三角 (2)倒三角  (3)菱形  (0)結束 ")
    try:
        x=int(s)
    except ValueError:
        print("請勿輸入非數字!!!")
        continue
    if (x < 0 or x > 3):
        print("請輸入 0-3 之間的數!")
        continue
    elif (x == 0):
        break
    
    while True:
        m=input("請選擇入每邊星星數：")
        try:
            n=int(m)
            n = 3 if n<3 else 8 if n>8 else n
            break                  #確認資料合理後,離開小迴圈，準備排圖案
        except ValueError:
            print("請勿輸入非數字!!!")
            continue
    
    s, t, str = "★", "　", ""     #多重指派 (全域變數，函數要使用需要加 global)
    if x==1:
        print(Chart1(n))
    elif x==2:
        print(Chart2(n))
    else:
        print(Chart3(n))
        

    
'''
以外迴圈皆為 i<=n 而言：
  1. 每列個數由小而大 如 j<=i   ;空白  k<=i 或 k<=i-1
  2. 每列個數由大而小 如 j<=n-i ;空白  k<=n 或 k<=n-1  
'''

