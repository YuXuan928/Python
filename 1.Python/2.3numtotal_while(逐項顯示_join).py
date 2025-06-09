
def create_str(n):
    list1 = [str(i).rjust(3, " ") for i in range(1, n+1)]  # 用空白填充左側
    rows = ["+".join(list1[i:i+10]) for i in range(0, len(list1), 10)]  # 每 10 個元素換行
    rows[0]=' '+rows[0]
    result = "\n+".join(rows)  # 用換行符號連接
    return result

n=1
while (n>0):
    n = int(input("請輸入大於1且小於101的正整數：<結束:0>"))
    if n<=0:
        continue

    n=2 if n==1 else 100 if n>200 else n
    st, sum = "", 0         #多重指派
    for i in range(1, n+1):
        sum += i
    st=create_str(n)
    print(st+"="+str(sum))
    print("1 到 %d 的整數和為 %d" % (n, sum))