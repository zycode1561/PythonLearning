class MyFirstClass:
    """帮助信息： 这是我的第一个class文件"""
    # 所有实例都会共享
    number = 100

    # name = str()
    # age = int()

    # 构造函数，初始化的方法，当创建一个类的时候，首先会调用它
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('number = ', self.number)

    def display_name(self):
        print(self.name)


myClass = MyFirstClass('Eric', [20, 18])
myClass.display()
myClass.display_name()
print('number = ', myClass.number)
print('age = ', myClass.age)
print('name = ', myClass.name)
print(myClass.__doc__)
print(myClass.__module__)
print(myClass.__dict__)


class MySecondClass(MyFirstClass):
    def __init__(self):
        print('调用子类的构造函数')


c = MyFirstClass('harry', [20, 30])
c.__setattr__('number', 200)
print(c.number)