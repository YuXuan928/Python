nat = input("請輸入國文成績：")
math = input("請輸入數學成績：")
eng = input("請輸入英文成績：")
sum = int(nat) + int(math) + int(eng)  #輸入值需轉換為整數
average = sum / 3
print("1. 百分比(%)表示法")
print("成績總分：%d，平均成績：%5.2f" % (sum, average))       #1.百分比(%)

print("2. f-string表示法")
print(f'成績總分：{sum}，平均成績：{average:5.2f}') #f-string 

print("3. str.format()表示法")
print("成績總分：{}，平均成績：{:.2f}".format(sum, average)) #str.format() 
input("Press any key to exit.")