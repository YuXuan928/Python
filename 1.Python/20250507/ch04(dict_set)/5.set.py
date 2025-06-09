persons = ["林小明","曾山水","鄭美麗","林小明","曾山水","林小明"]
print(f'\n#1.串列 persons ={persons}')

s = set(persons) # 串列轉集合
print(f'\n#2.串列轉set(集合) s=set(persons) => {s}')
# {'林小明', '曾山水', '鄭美麗'} #集合中的元素是唯一的(不重複)

list1 = list(s)  # 集合轉串列
print(f'\n#3.集合轉串列 list1=list(s) => {list1}') # ['林小明', '曾山水', '鄭美麗']

print(f'\n#4.使用index=0 取第1個串列元素 list1[0]={list1[0]}')
   