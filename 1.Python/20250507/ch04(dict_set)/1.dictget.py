dict1 = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
name = input("輸入要查詢的血型:")
blood = dict1.get(name)     #!!(1)以鍵找值get(key)

#1.使用 以鍵找'值'=>get(key) 判斷
print("#1.使用 以鍵找值 [dict1.get(key)] 判斷")
if blood == None:  
    print("沒有「" + name + "」血型！")
else:  
    print(name + " 血型的個性為：" + str(dict1[name])) #str() 可以免

#2.使用 以鍵(key) 判斷是否在 dict1 內
print("\n#2.以鍵(key) 判斷是否在 [if name in dict1:] 內")
if name in dict1 :          #!!(2) if name in dict1
    print(name + " 血型的個性為：" + str(dict1[name])) #str() 可以免
else:  
    print("沒有「" + name + "」血型！")
   
#3.使用以鍵(key) 判斷是否在 [if name in dict1.keys() 內
print("\n#3.使用以鍵(key) 判斷是否在 [if name in dict1.keys() 內")
if name in dict1.keys() :   ##!!(3) if name in dict1.keys()
    print(name + " 血型的個性為：" + str(dict1[name])) #str() 可以免
else:  
    print("沒有「" + name + "」血型！")
    
#巡覽dict1.items()、巡覽dict1.keys()、巡覽dict1.valus()
print('\n#4.巡覽dict1.items()')
for key, val in dict1.items():    
    print(f'{key:2} {val}')   

print('\n#5.巡覽dict1.keys()')
for key in dict1.keys():
    print(key)

print('\n#6.巡覽dict1.valus()')
for val in dict1.values():
    print(val)    
    
#input("Press any key to exit.")