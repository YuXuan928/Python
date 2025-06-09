# =============================================================================
# #多型允許「不同類別」的物件，在相同方法名稱下有不同的實作方式。
# 
# 
# #一般類別
# class Animal:
#     def speak(self):
#         print("某種動物在發出聲音")
# 
# class Dog(Animal):
#     def speak(self):
#         print("狗：汪汪！")
# 
# class Cat(Animal):
#     def speak(self):
#         print("貓：喵喵！")
# 
# def animal_speak(animal):
#     animal.speak()  # 不論傳入哪種動物，都呼叫對應的 speak()
# 
# #物件建立
# Lucky=Dog()
# Luna=Cat()
# 
# #一般用法
# print('一般用法：1.Lucky.speak()➡', end=' ')
# Lucky.speak()    #狗：汪汪！
# print('一般用法：2.Luna.speak()➡', end=' ')
# Luna.speak()      #貓：喵喵！
# 
# #多形用法
# print('多形用法：1.animal_speak(Lucky)➡', end=' ')
# animal_speak(Lucky)  # 狗：汪汪！
# print('多形用法：2.animal_speak(Luna)➡', end=' ')
# animal_speak(Luna)  # 貓：喵喵！
# =============================================================================
# 🧪 多型挑戰題：動物行為總動員！
# ✅ 題目說明：
# 請你設計一個動物系統，所有動物都能「說話」(speak()) 和「移動」(move())，但每種動物的行為都不同。
# 🔹 父類別 Animal
# 方法（不實作，只定義）：
# speak()：說話
# move()：移動
# ✅ 提示：你可以在 Animal 中使用 pass 表示不實作，讓子類別自行定義。
# 🔹 子類別：
# Dog
# speak() ➜ 「狗：汪汪！」
# move() ➜ 「狗用四腳奔跑」
# 
# Cat
# speak() ➜ 「貓：喵喵～」
# move() ➜ 「貓悄悄地走路」
# 
# Duck
# speak() ➜ 「鴨子：嘎嘎！」
# move() ➜ 「鴨子在水上滑行」
# 
# 📝 要求：
# 建立每種動物的物件（例如：d1, c1, du1）
# 放入一個 animals 列表中
# 用一個 for 迴圈讓每隻動物依序：
# 說話（.speak()）
# 移動（.move()）
# 
# ✅ 預期輸出範例：
# 狗：汪汪！
# 狗用四腳奔跑
# 貓：喵喵～
# 貓悄悄地走路
# 鴨子：嘎嘎！
# 鴨子在水上滑行
# =============================================================================
class Animal():
    def __init__(self):
        pass
    def speak (self) :
        pass
    def move (self):
        pass
    
class Dog(Animal):
    def speak (self):
        print("狗:汪汪!")
    def move (self):
        print("狗用四腳奔跑")
        
class Cat(Animal):
    def speak(self):
        print("貓:喵喵~")
    def move (self):
        print("貓悄悄地走路")

class Duck(Animal):
    def speak(self):
        print("鴨子:嘎嘎!")        
    def move(self):
        print("鴨子在水上滑行")
        
d1 = Dog()
c1 = Cat()
du1 = Duck()

animals = [d1, c1, du1]

for animal in animals:
    animal.speak()
    animal.move()       



















































