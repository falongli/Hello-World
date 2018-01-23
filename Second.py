#coding:utf-8
import re
from os import path
import sys
"""
the second python program
"""

sTemp = 'haha'
print(sTemp)

def OneFunc():
    s = 'bee'

    def innerFunc():
        print('innerFunc')
        return None

    innerFunc()
    bLocal = 'innerFunc' in locals()
    print('innerFunc is local function:{0}'.format(bLocal))
    return  None

OneFunc()
bGlobal = 'OneFunc' in globals()
print('OneFunc is local function:{0}'.format(bGlobal))


fs = [(lambda n, i=i: i + n) for i in range(10)]
print(fs[4](3))
print(fs[5](3))
print(fs[9](3))

varDic = dict(vars())

for item in varDic.items():
    print("{0}:{1}".format(item[0], item[1]))



class TestDemo(object):
    """
    Python变量命名用法（以字符或者下划线开头，可以包括字母、数字、下划线，区别大小写）
    一般变量
    常量
    私有变量
    内置变量
    """
    FINAL_VAR = "V1.0" # 常量，不可修改的变量，以大写字母或加下划线命名，这个只是约定，即使更改了也不会报错

    class_name = "TestDemo" # 常见变量命名，

    __maker__ = 'libingxian' # 内置变量，两个前置下划线和两个后置下划线，内置对象所具有，声明时不可与内置变量名的重复

    def __init__(self):
        self.__private_var = "private" # 私有变量，以两个前置下划线开头，只能在本类中使用，类外强制访问会报错
        self.public_var = "public" # 一般变量

    def __private_method(self):# 私有方法，以两个下划线开头、字母小写，只能在本类中使用，类外强制访问会报错
        print("i am private")

    def public_method(self):
        print("i am public")

test_demo = TestDemo()
print(test_demo.FINAL_VAR) # 访问常量
print(test_demo.public_var) # 访问一般变量
print(test_demo.__maker__)
#print(test_demo.__private_var)# 访问私有变量，运行会报错
#test_demo.__private_method() # 访问私有方法，运行会报

#以两个下划线开头的变量和方法均为私有，不可在外部进行访问


sPath = __file__
print(sPath)
sDir = path.dirname(sPath)
print(sDir)
sFileName = path.basename(sPath)
print(sFileName)

for i in sys.path:
    print(i)