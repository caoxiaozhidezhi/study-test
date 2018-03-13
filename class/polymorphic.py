# _*_ coding:utf-8 _*_


# ==================多态专题==================
"""
定义person类，并且封装一个和狗玩的方法
在方法内部，直接让狗对象调用game方法
"""


class Dog(object):
    """docstring for Dog"""

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):
    """docstring for XiaoTianDog"""

    def game(self):
        print("%s飞到天上去" % self.name)


class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s快乐的玩耍" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)

"""
案例总结：
person类中只需要让狗对象调用game方法，而不关心具体是什么狗
game方法是在Dog父类中定义的
在程序执行时，传入不同的狗对象实参，就会产生不同的执行效果
"""


# ==================类属性和实例属性==================
"""
类属性就是给类对象中定义的属性
通常用来记录与这个类相关的特性
类属性不会用于记录具体对象的特性
"""


class Tool(object):
    """docstring for Tool"""
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, arg):
        self.arg = arg

        # 让类属性的值+1
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

print(Tool.count)
