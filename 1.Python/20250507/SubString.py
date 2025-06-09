

st = "ABCDEFGHIJ"
print(f'字串 st={st}')
n=len(st)
print(f'長度 n={n}\n')

print(f'st[3]={st[3]}')           #取index 3 一個
print(f'st[4]={st[4]}')           #取index 4 一個
print(f'st[:3]={st[:3]}')         #取前3個
print(f'st[:4]={st[:4]}')         #取前4個
print(f'st[:-1]={st[:-1]}')       #由開始 - 最後一個排除 => index 0 - 8 (n-2)
print(f'st[0:8]={st[0:8]}')       #index取 0 - 7
print(f'st[2:7]={st[2:7]}')       #index取 2 - 6
print(f'st[4:-1]={st[4:-1]}')     #index取 4 - 最後一個排除 => index 3 - 8 (n-2)
print(f'st[3:]={st[3:]}')         #index取 3 到尾 
print(f'st[-5:-1]={st[-5:-1]}')   #index取 到數第6個 - 最後一個排除 => index (n-6=4) - (n-2=8)


print()
#slice(start, stop, step)
print(f'st[slice(3,4)]={st[slice(3,4)]}')       #取index 3 一個
print(f'st[slice(4,5)]={st[slice(4,5)]}')       #取index 4 一個
print(f'st[slice(3)]={st[slice(3)]}')           #取前3個
print(f'st[slice(4)]={st[slice(4)]}')           #取前4個
print(f'st[slice(-1)]={st[slice(-1)]}')         #由開始 - 最後一個排除 => index 0 - 8 (n-2)
print(f'st[slice(0, 8)]={st[slice(0, 8)]}')     #index取 0 - 7
print(f'st[slice(2, 7)]={st[slice(2, 7)]}')     #index取 2 - 6
print(f'st[slice(4, -1)]={st[slice(4, -1)]}')   #index取 4 - 最後一個排除 => index 3 - 8 (n-2)
print(f'st[slice(3, n)]={st[slice(3, n)]}')     #index取 3 到尾
print(f'st[slice(-5, -1)]={st[slice(-5, -1)]}') #index取 到數第6個 - 最後一個排除 => index (n-6=4) - (n-2=8)

#上方二種方式10題功能相同，但注意用法差異