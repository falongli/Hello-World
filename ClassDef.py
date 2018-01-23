#coding:utf-8
# class Fruit:
#     price = 0               # 类属性
#
#     def __init__(self):
#         self.color = "red"  # 实例属性
#         zone = "China"      # 局部变量
#
# if __name__ == "__main__":
#     print(Fruit.price)      # 使用类名调用类变量
#     apple = Fruit()         # 实例化apple
#     print(apple.color)
#     Fruit.price = Fruit.price + 10
#     print("apple's price:" + str(apple.price))
#     banana = Fruit()
#     print("banana's price:" + str(banana.price))

# 访问私有属性
# class Fruit:
#     def __init__(self):
#         self.__color = "red"
#
# if __name__ == "__main__":
#     apple = Fruit()
#     print(apple._Fruit__color)

# 常见内置属性的方法
# class Fruit:
#     def __init__(self):
#         self.__color = "red"    # 定义私有变量
#
# class Apple(Fruit):     # Apple继承了Fruit
#     """This is doc"""
#     pass
#
# if __name__ == "__main__":
#     fruit = Fruit()
#     apple = Apple()
#     print(Apple.__bases__)      # 输出基类组成的元组
#     print(apple.__dict__)       # 输出属性组成的字典
#     print(apple.__module__)     # 输出类所在的模块名
#     print(apple.__doc__)        # 输出doc文档

# class Fruit:
#     price = 0                                   # 类变量
#
#     def __init__(self):
#         self.__color = "red"                      # 定义私有变量
#
#     def getColor(self):
#         print(self.__color)
#
#     # @ staticmethod                              # 使用@staticmethod修饰器静态方法
#     # def getPrice():
#     #     print(Fruit.price)
#     #
#     # def __getPrice():                            # 定义私有函数
#     #     Fruit.price = Fruit.price + 10
#     #     print(Fruit.price)
#
#     @ classmethod                              # 使用@classmethod修饰器静态方法
#     def getPrice(cls):
#         print(cls.price)
#
#     def __getPrice(cls):                            # 定义私有函数
#         cls.price = cls.price + 10
#         print(cls.price)
#
#
#     count = classmethod(__getPrice)      # 使用staticmethod方法定义静态方法
#
# if __name__ == "__main__":
#     apple = Fruit()                              # 实例化apple
#     apple.getColor()                            # 使用实例调用静态方法
#     Fruit.count()                                # 使用类名调用静态方法
#     banana = Fruit()
#     Fruit.count()
#     Fruit.getPrice()

# 内部类的使用
# class Car:
#     class Door:                 # 内部类
#         def open(self):
#             print("open door")
#
#     class Wheel:                # 内部类
#         def run(self):
#             print("car run")
#
# if __name__ == "__main__":
#     car = Car()
#     backDoor = Car.Door()       # 内部类的实例化方法一,object_name = outclass_name.inclass_name()
#     frontDoor = car.Door()      # 内部类的实例化方法二,先实例化外部类，再实例化内部类
#     backDoor.open()
#     frontDoor.open()
#     wheel = Car.Wheel()
#     wheel.run()

# __init__方法
# class Fruit:
#     def __init__(self, color):
#         self.__color = color
#         print(self.__color)
#
#     def getColor(self):
#         print(self.__color)
#
#     def setColor(self, color):
#         self.__color = color
#         print(self.__color)
#
# if __name__ == "__main__":
#     color = "red"
#     fruit = Fruit(color)        # 带参数的构造函数
#     fruit.getColor()
#     fruit.setColor("blue")

# __del__方法
# class Fruit:
#     def __init__(self, color):
#         self.__color = color
#         print(self.__color)
#
#     def __del__(self):
#         self.__color = ""
#         print("free ...")
#
#     def grow(self):
#         print("grow ...")
#
# if __name__ == "__main__":
#     color = "red"
#     fruit = Fruit(color)
#     fruit.grow()

# 使用gc模块显示调用垃圾回收器
# import gc
#
# class Fruit:
#     def __init__(self, name, color):
#         self.__name = name
#         self.__color = color
#
#     def getColor(self):
#         return self.__color
#
#     def setColor(self, color):
#         self.__color = color
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         self.__name = name
#
# class FruitShop:
#     def __init__(self):
#         self.fruits = []
#
#     def addFruit(self, fruit):
#         fruit.parent = self         # 把Fruit类关联到Fruitshop类
#         self.fruits.append(fruit)
#
# if __name__ == "__main__":
#     shop = FruitShop()
#     shop.addFruit(Fruit("apple", "red"))
#     shop.addFruit(Fruit("banana", "yellow"))
#     print(gc.get_referents(shop))       # 打印出shop关联的所有对象
#     del shop
#     print(gc.collect())     # 显示调用垃圾回收机制

# __new__()在__init__()之前被调用，用于创建实例对象
# class Singleton(object):
#     __instance = None       # 定义实例
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):      # 在__init__之前调用
#         if Singleton.__instance is None:    # 生成唯一实例
#             Singleton.__instance = object.__new__(cls, *args, **kwargs)
#         return Singleton.__instance

# class Fruit(object):
#     def __init__(self, color = "red", price = 0):
#         self.__color = color
#         self.__price = price
#
#     def __getattribute__(self, name):               # 获取属性的方法
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):             # 设置属性的方法
#         self.__dict__[name] = value
#
# if __name__ == "__main__":
#     fruit = Fruit("blue", 10)
#     print(fruit.__dict__.get("_Fruit_color"))   # 获取color属性的值
#     fruit.__dict__["_Fruit_price"] = 5      # 使用__dict__进行赋值
#     print(fruit.__dict__.get("_Fruit_price"))

# class FruitShop:
#     def __init__(self):
#         self.fruits = []
#
#     def __getitem__(self, i):   # 获取水果店的水果
#         return self.fruits[i]
#
# if __name__ == "__main__":
#     shop = FruitShop()
#     shop.fruits = ["apple", "banana"]   # 给fruit赋值
#     print(shop[1])
#     for item in shop:       # 输出水果店水果
#         print(item)

# __str__()用于表示对象的含义，返回一个字符串
# class Frutit:
#     '''Fruit类'''
#     def __str__(self):      # 定义对象的字符串表示
#         return self.__doc__ # 返回heredoc
#
# if __name__ == "__main__":
#     fruit = Frutit()
#     print(str(fruit))       # 调用__str__
#     print(fruit)            # 同丄行结果相同

# __call__()
# class Fruit:
#     class Growth:           # 内部类
#         def __call__(self):
#             print("grow ...")
#
#     grow = Growth()         # 返回__call__内容
#
# if __name__ == "__main__":
#     fruit = Fruit()
#     fruit.grow()            # 使用实例调用
#     Fruit.grow()            # 使用类名调用

# 动态添加方法
# class Fruit:
#     pass
#
# def add(self):      # 定义在内外的函数
#     print("grow ...")
#
# if __name__ == "__main__":
#     Fruit.grow = add        # 动态添加add函数
#     fruit = Fruit()
#     fruit.grow()

# 动态更新方法
# class Fruit():
#     def grow(self):
#         print("grow ...")
#
# def update():
#     print("update grow ...")
#
# if __name__ == "__main__":
#     fruit = Fruit()
#     fruit.grow()
#     fruit.grow = update   # 将grow方法更新为update()
#     fruit.grow()

# class Fruit():
#     def __init__(self, color):
#         self.color = color
#         print("fruit's color:%s" % self.color)
#
#     def grow(self):
#         print("grow ...")
#
# class Apple(Fruit):
#     def __init__(self, color):
#         Fruit.__init__(self, color)
#         print("apple's color:%s" % self.color)
#
# class Banana(Fruit):
#     def __init__(self, color):
#         Fruit.__init__(self, color)     # 显示调用父类构造函数
#         print("banana's color:%s" % self.color)
#
#     def grow(self):         # 覆盖父类方法
#         print("banana grow ...")
#
# if __name__ == "__main__":
#     apple = Apple("red")
#     apple.grow()
#     banana = Banana("yellow")
#     banana.grow()

# 使用super()调用父类
# class Fruit(object):    # 定义基类，继承自object，python3.x中不是必须的
#     def __init__(self):
#         print("parent")
#
# class Apple(Fruit):
#     def __init__(self):
#         super(Apple, self).__init__()   # 使用super调用父类，更直观
#         print("child")
#
# if __name__ == "__main__":
#     Apple()

# from abc import ABCMeta, abstractmethod     # 引入所需的module
#
#
# class Fruit():     # 抽象类
#     __metaclass__ = ABCMeta
#     @abstractmethod     # 使用@abstractmethod修饰器定义抽象函数
#     def grow(self):
#         pass
#
#
# class Apple(Fruit):
#     def grow(self):     # 子类中必须重写抽象函数
#         print("Apple growing")
#
# if __name__ == "__main__":
#     apple = Apple()
#     apple.grow()
#     # fruit = Fruit()

# 多态性
# class Fruit:
#     def __init__(self, color = None):
#         self.color = color
#
# class Apple(Fruit):
#     def __init__(self, color = "red"):
#         Fruit.__init__(self, color)
#
# class Banana(Fruit):
#     def __init__(self, color = "yellow"):
#         Fruit.__init__(self, color)
#
# class FruitShop:
#     def sellFruit(self, fruit):
#         if isinstance(fruit, Apple):
#             print("sell apple")
#         if isinstance(fruit, Banana):
#             print("sell banana")
#         if isinstance(fruit, Fruit):
#             print("sell fruit")
#
# if __name__ == "__main__":
#     shop = FruitShop()
#     apple = Apple("red")
#     banana = Banana("yellow")
#     shop.sellFruit(apple)
#     shop.sellFruit(banana)

# 多重继承
# class Fruit:
#     def __init__(self):
#         print("initialize Fruit")
#
#     def grow(self):
#         print("grow...")
#
# class Vegetable(object):
#     def __init__(self):
#         print("initialize Vegetable")
#
#     def plant(self):
#         print("plant...")
#
# class Watermelon(Fruit, Vegetable):
#     pass
#
# if __name__ == "__main__":
#     w = Watermelon()
#     w.grow()
#     w.plant()

# Mixin混合类
# class Fruit(object):                            # 水果
#     def __init__(self):
#         pass
#
# class HuskedFruit(object):               # 削皮水果
#     def __init__(self):
#         print("initialize HuskedFruit")
#
#     def husk(self):                     # 削皮方法
#         print("husk...")
#
# class DecorticatedFruit(object):         # 剥皮水果
#     def __init__(self):
#         print("initialize DecorticatedFruit")
#
#     def decorticat(self):               # 剥皮方法
#         print("decorticat...")
#
# class Apple(HuskedFruit, Fruit):
#     pass
#
# class Banana(DecorticatedFruit, Fruit):
#     pass

# 运算符重载
# class Fruit:
#     def __init__(self, price = 0):
#         self.price = price
#
#     def __add__(self, other):   # 重载加号运算符
#         return self.price + other.price
#
#     def __gt__(self, other):    # 重载大于运算符
#         if self.price > other.price:
#             flag = True
#         else:
#             flag = False
#         return flag
#
# class Apple(Fruit):
#     pass
#
# class Banana(Fruit):
#     pass
#
# if __name__ == "__main__":
#     apple = Apple(3)
#     print "苹果的价格:", apple.price
#     banana = Banana(2)
#     print "香蕉的价格:", banana.price
#     print(apple > banana)
#     total = apple + banana
#     print "合计:", total

# 对运算符<<的重载
# import sys
#
# class Stream:
#     def __init__(self, file):
#         self.file = file
#
#     def __lshift__(self, other):    # 对运算符<<重载
#         self.file.write(str(other))
#         return self
#
# class Fruit(Stream):
#     def __init__(self, price=0, file=None):
#         Stream.__init__(self, file)
#         self.price = price
#
# class Apple(Fruit):
#     pass
#
# class Banana(Fruit):
#     pass
#
# if __name__ == "__main__":
#     apple = Apple(2, sys.stdout)    # apple对象可作为流输出
#     banana = Banana(3, sys.stdout)
#     endl = "\n"
#     apple << apple.price << endl        # 使用重载后的<<运算符
#     banana << banana.price << endl

# 工厂方法
# class Factory:      # 工厂类
#     def createFruit(self, fruit):
#         if fruit == "apple":
#             return Apple()
#         elif fruit == "banana":
#             return Banana()
#
# class Fruit:
#     def __str__(self):
#         return "fruit"
#
# class Apple(Fruit):
#     def __str__(self):
#         return "apple"
#
# class Banana(Fruit):
#     def __str__(self):
#         return "banana"
#
# if __name__ == "__main__":
#     factory = Factory()
#     print(factory.createFruit("apple"))     # 创建apple对象
#     print(factory.createFruit("banana"))

# 自定义异常
# from __future__ import division
#
# class DivisionException(Exception):
#     def __init__(self, x, y):
#         Exception.__init__(self, x, y)
#         self.x = x
#         self.y = y
#
# if __name__ == "__main__":
#     try:
#         x = 3
#         y = 2
#         if x % y > 0:
#             print(x / y)
#             raise DivisionException(x, y)   # 抛出异常
#     except DivisionException, div:
#         print("DivisionException: x / y %.2f" % (div.x / div.y))

# assert用于检测某个条件表达式是否为真
# t = ("hello",)
# assert len(t) >= 1
# t = ("hello")   # 无逗号，作为字符串处理，len=5
# assert len(t) == 1

# 带message的assert语句
# month = 13
# assert 1 <= month <= 12, "month errors"

# 异常信息
# def fun():
#     a = 10
#     b = 0
#     return a / b
#
# def format():       # 格式化输出
#     print("a / b =" + str(fun()))
#
# if __name__ == "__main__":
#     format()

import sys
try:
    x = 10 / 0
except Exception as ex:
    print(ex)
    print(sys.exc_info())