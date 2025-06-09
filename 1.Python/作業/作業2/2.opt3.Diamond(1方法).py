def diamond2(n, back, m):#n:菱形邊長；back=1 (有背景)  m:外框線寬  (不同方法供參考)
    #int i, j, k, x, y;
    s = '★'
    t = '☆' if back==1 else '　'
    str = ''
    #**本案例將 t="　" 替代 t = "☆"，結果同Diamond1
    y = 1                                      #x:列值號範圍：1,2,3,4,5,4,3,2,1  ；y=2*x-1為星星數；    
    for i in range(1,2 * n):
        for j in range(1,2 * n):
            #k = (2 * n - y) / 2               #k為每一列實心星星的起始位置 k = 5, 4, 3, 2, 1, 2, 3, 4, 5
            k=n + 1 - i if i <= n else i - n + 1; #同
            str += s if (j >= k and j < (k + y) and (j < (k + m) or j > (2 * n - k - m))) else t
            #str = str + s if(j >= k and j < (k + y)) else str + t  #菱形部份實心，其餘兩邊空白星
            #j >= k && j < (k + x)即為菱行的範圍(本處j為一般的起始位置)
        y = y + 2 if i < n else y - 2;        #**本式功能同y = 2 * (n - abs(n - i)) - 1; ，但位置不能改變
        str += "\n";
    return str

#main 主程式
n=6
while (n>2):
    n = int(input("請輸入 大於2且小於13 的正整數：<0:結束>"))
    if n==0:
        continue
    n=3 if(n<3) else n
    n=12 if(n>12) else n
    back=0
    #while back>=0 :
    back= int(input("請選擇 0)無背景；  1)有背景  -1)結束 :")) #background selected
    if back==-1:
        n=0
        break
    back = 1 if back>=1 else 0 
    m = int(input("請選擇邊框數 1 <= m < n (邊長) :"))
    m = 1 if m<1 else m
    m = n-1 if m>=n else m
    print('m=', m)
    print('back=', back)
    print(diamond2(n, back, m))
	
