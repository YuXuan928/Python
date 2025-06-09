#使用1個函數處理3個形狀選項

def ShowChart(n, x):
    #i, j, k, y, z   #y為z的終值，z為外迴圈的變數；j,k內迴圈的變數；i為控制j,k的重要控制變數
    s, t, str = "★", "　", ""
    i = n if x==2 else 1              #x==2倒▽時 i=n, 其他(x=1或x=3) i=1
    y = 2 * n - 1 if x == 3 else n;   #x==3菱形時 y=2*n-1(跑2*n-1圈)；其他(x=1或x=2) y=n(跑n圈)
    for z in range(1, y+1):
        #!!以下式 '　'*(n-i) [加空白] + (s+t)*i [加一個星及一個空白] 
        str+=('　'*(n-i) + (s+t)*i)      #同上二迴圈功能
        str += "\n"
    
        if (x == 3):                     #菱形時:
            i = i+1 if z < n else i - 1  #上半段i遞增；下半段i遞減
        else:
            i= i+1 if x==1 else i-1 if x==2 else i    #x==1時,正△i遞增；x == 2時,倒▽i遞減
    return str

while True:
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
            break           #確認資料合理後,離開小迴圈，準備排圖案
        except ValueError:
            print("請勿輸入非數字!!!")
            continue
    print(f'\n形狀：{x}; 邊數：{n}\n{ShowChart(n, x)}')


'''
以外迴圈皆為 i<=n 而言：
  1. 每列個數由小而大 如 j<=i   ;空白  k<=i、k<=i-1
  2. 每列個數由大而小 如 j<=n-i ;空白  k<=n、k<=n-1  
'''

