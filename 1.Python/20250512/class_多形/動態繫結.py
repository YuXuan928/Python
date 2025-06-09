#多型允許「不同類別」的物件，在相同方法名稱下有不同的實作方式。
#使用抽象類別+動態繫結以達到多形功能
from abc import ABC, abstractmethod

# 抽象類別
class Animal(ABC):
    def __init__(self, name):
        self.name = name
        print(f"[Animal 建構] 建立 Animal 子類：{self.__class__.__name__}，名稱：{self.name}")

    @abstractmethod     #抽象方法
    def speak(self):
        pass            #沒有實作

# 子類別 Dog
class Dog(Animal):
    def speak(self):
        print(f"[Dog.speak()] {self.name} 說：汪汪")

# 子類別 Cat
class Cat(Animal):
    def speak(self):
        print(f"[Cat.speak()] {self.name} 說：喵喵")

# 動態繫結的函式 animal: Animal 是 型別註解（type annotation）
def animal_talk(animal: Animal):    #
    print(f"\n[animal_talk()] 現在呼叫的是：{animal.__class__.__name__} 的 speak() 方法")
    animal.speak()

# 建立子類別的實例（完成實作）
animals = [
    Dog("Lucky"),
    Cat("Luna")
]

# 執行多型呼叫
for a in animals:
    animal_talk(a)



'''
寫法	                   意思
==================    ==========================================
animal: Animal	      animal 是 Animal 類別的實例型別（或其子類別）
class Dog(Animal):	  Dog 類別「繼承」Animal 類別
a = Animal()	      a 是一個 Animal 類別的「物件實例」
def func(x: int)	  x 是整數型別，這是型別註解（非限制）

'''