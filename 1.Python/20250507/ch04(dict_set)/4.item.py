# dict1.items() 再轉list方便使用迭代
dict1={"金牌":26, "銀牌":34, "銅牌":30}
item1 = list(dict1.items())  #使用items取得字典中的name, num2個items的指定變數 
#item1 = dict1.items()       #本式在迴圈 in 時同上式，但不能像上式使用迭代

print('#1.dict1.items()的內容')
for name, num in item1:      #items 支援 in；因此不使用 index 
    #print("得到的 %s 數目為 %d 面" % (name, num))
    print(name, num)
    
key1=dict1.keys()
print("\n#2.鍵(keys)內容：")
for name in key1:           #keys、values、items 支援 in 
    print(name, end=" ")
print()
value1=dict1.values()
print("\n#3.值(values)內容：")
for num in value1:          #keys、values、items 支援 in 
    print(num, end=" ")  
print()  
print("\n#4.key1的內容")
print(key1)
print("\n#5.value1的內容")
print(value1)

#---增列 #下段迭代用法在使用line3(不使用line4)
print('\n##使用轉成串列可以使用迭代')
print(f'#1.item1[1]={item1[1]}')
print(f'#2.item1[1][0]={item1[1][0]}') #!!本式在使用line3(不使用line4)
print(f'#3.item1[1][1]={item1[1][1]}') #!!本式在使用line3(不使用line4)
print("\n##使用for..for..print(item1[i][j],end=' ') 雙迴圈顯示內容")
for i in range(len(dict1)):
    for j in range(2):
        print(item1[i][j], end=' ')
    print()


print('\n##dict.setdefault(,)運用')
dict1={"香蕉":20, "蘋果":50, "橘子":30}
print(f'dict1={dict1}')
print('\n#1.dict1.setdefault("蘋果",60) 給value=60')
n=dict1.setdefault("蘋果",60) #鍵、值皆存在 n=50不會改變60
print(f'dict1={dict1}  #蘋果給值60 value仍然為 50' )

print('\n#2.dict1.setdefault("鳳梨") #增加 key 鳳梨 ')
n=dict1.setdefault("鳳梨") #鍵增加'鳳梨'、值 n=None
print(f'dict1={dict1}  #鳳梨沒有給值 value為 None')

print('\n#3.dict1.setdefault("鳳梨",100) #鳳梨給值100 ' )
n=dict1.setdefault("鳳梨",100) #鍵增加'鳳梨'、值n=100 #!!(但先執行上式n=None，不會變10)
print(f'dict1={dict1}  #鳳梨給值100 value仍然為 None')




#input("Press any key to exit.")