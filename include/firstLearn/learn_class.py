#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问

# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student:
    # __slots__ = ('name', 'age', 'score')

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score!')


def __str__(self):
    # return 'Student name : {}, age : {}'.format(self.name, self.age)
    return 'Student name : %s, age : %d' % (self.name, self.age)


myClass = Student('zhang', 12, 100)

print(myClass)
print(myClass.name, myClass.age, myClass.get_score())
# myClass.set_score(200)
# print(myClass.name, myClass.age, myClass.get_score())

a = 1
b = 2
c = a // b
# / 表示浮点数除法， //表示整数除法
a, b = b, a
print(a, b, c)
print(max(a, b, c))
