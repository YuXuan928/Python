
'''
#(1)使用二個 input
a=int(input("請輸入整數 a："))
b=int(input("請輸入整數 b："))
'''

#(2)使用多值輸入 (預設空白作分隔)
a, b = map(int, input("請輸入 a, b：<使用空格分隔二數>").split())

print("二數相加 = " + str(a+b))
print("二數相減 = " + str(a-b))
input("Press any key to exit.")






