set1={"Python","Java","Kotlin"} #set
enum1=enumerate(set1) # 轉換為 enumerate 物件
print(f'\n#1.集合 set1 ={set1}')

print(f'\n#2.集合轉列舉 enum1=enumerate(set1) {type(enum1)}')
#print(type(enum_langs))     # <class 'enumerate'>

# 轉成串列
print('\n#3.enumerate轉換成串列顯示 print(list(enum1))')
print(list(enum1)) # [(0, 'Python'), (1, 'Kotlin'), (2, 'Java')]
# 以迴圈輸出
print('\n#4.經由for迴圈顯示 enum1 (自帶enum1序號)')
for item in enumerate(set1):   # 集合必須轉換為 enumerate 物件,才能使用 for 讀取
    print(item)
print('\n#5.經由for迴圈顯示 enum1 內容 (另帶enum1序號)')
for i,item in enumerate(set1):
    print(i,item)    
