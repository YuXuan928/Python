#作業二題目一


def s1(n):
    
    star = '★'
    space = '　'
    lines = []
    for i in range(1, n+1):
        
        lead = space * (n - i)
        
        body = (star + space) * i
        lines.append(lead + body)
    return '\n'.join(lines)

# =============================================================================
# i 表示第幾行（從上往下）
# 
# 用 space * (n - i) 產生左側空白，使三角形置中
# 
# body 用 (★ + 空格) 重複 i 次
# 
# 每一行放進 lines 陣列，最後用 join 組合為多行字串
# =============================================================================


def s2(n):
    
    star = '★'
    space = '　'
    lines = []
    for i in range(n, 0, -1):
        lead = space * (n - i)
        body = (star + space) * i
        lines.append(lead + body)
    return '\n'.join(lines)


def s3(n):
    
    top = s1(n)
    
    bottom_lines = []
    star = '★'
    space = '　'
    for i in range(n-1, 0, -1):
        lead = space * (n - i)
        body = (star + space) * i
        bottom_lines.append(lead + body)
    return '\n'.join([top] + bottom_lines)


def main():
    while True:
        choice = input("請選擇 (1)正三角 (2)倒三角 (3)菱形 (0)結束：")
        if choice not in {'0','1','2','3'}:
            print("請輸入 0-3 之間的數字！")
            continue
        if choice == '0':
            print("程式結束。")
            break

        # get n
        while True:
            try:
                n = int(input("請輸入每邊星星數 (3-8)："))
                if n < 3:
                    n = 3
                elif n > 8:
                    n = 8
                break
            except ValueError:
                print("請勿輸入非數字！")

        if choice == '1':
            print("(1)正三角形")
            print(s1(n))
        elif choice == '2':
            print("(2)倒三角形")
            print(s2(n))
        else:
            print("(3)菱形")
            print(s3(n))

if __name__ == '__main__':
    main()
