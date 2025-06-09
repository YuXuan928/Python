def sayHello():
    print("Hello")
    
def IsLeap(y):
    tf = False
    if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        tf=True
    msg=f'{y:4d}:是閏年!' if tf==True else f'{y:4d}不是閏年!'
    return msg   