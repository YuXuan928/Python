dict1={"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())        #取出字點的keys(鍵)成為 list
listvalue = list(dict1.values())    #取出字點的values(值)成為 list
for i in range(len(listkey)):
    print(f"得到的 {listkey[i]:2s} 數目為 {listvalue[i]:3d} 面")
    #print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))


print("\n#使用 [for item in listkey 或(listvalue):]\n\t 顯示鍵(keys)以及值(value)的內容：")
for item in listkey:           #keys、values、items 支援 in 
    print(item, end=" ")
print("")
for item in listvalue:         #keys、values、items 支援 in 
    print(item, end=" ")

#直接顯示  listkey、listvalue 內容  
print("\n\n#直接顯示  listkey、listvalue 內容")    
print("#1.listkey的內容")
print(listkey)
print("\n#2.listvalue的內容")
print(listvalue)    
#input("Press any key to exit.")
