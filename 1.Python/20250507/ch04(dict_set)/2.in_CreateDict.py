
print('#建立字典的3種方式：')
print('#1.dict1 = {"林小明":85, "曾山水":93, "鄭美麗":67}')          #方式1
print('#2.dict1=dict([ ["林小明",85], ["曾山水",93],["鄭美麗",67]]') #方式2
print('#3.dict1=dict(林小明=85, 曾山水=93, 鄭美麗=67)') #鍵 不使用引號   #方式3 
dict1=dict(林小明=85, 曾山水=93, 鄭美麗=67)          #鍵(key)不使用引號    
name = input("輸入學生姓名：")
if name in dict1:               #判斷 name 是否 in 字典中
    print(name + "的成績為 " + str(dict1[name]))
else:  
    score = int(input("輸入學生分數："))
    dict1[name] = score                 #使用 score(value)指派給 name(key)
    print("字典內容：" + str(dict1))
    
#input("Press any key to exit.")
