# _*_ coding:utf-8 _*_
class Women:
    """docstring for Women"""

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部是可以访问对象的私有属性的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 私有属性在外界不能被直接访问
# print xiaofang.__age
# 私有方法同样不允许在外界直接访问
# xiaofang.__secret()

# python中没有真正的私有属性和方法，通过加上“_类名”+私有属性/私有方法，一样可以调用
print(xiaofang._Women__age)
xiaofang._Women__secret()
print("")


# ==================父类的私有属性和私有方法==============
class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法%d" % self.__num2)
        self.__test()


class B(A):

    def demo(self):

        # 在子类的对象方法中，不能访问父类的私有属性
        # print "访问父类的私有属性%d" % self.__num2
        # 调用父类的私有方法
        # self.__test

        # 访问父类的公有属性
        print("子类方法%d" % self.num1)
        # 调用父类的公有方法
        self.test()

        pass


b = B()
print(b)

b.demo()

# 在外界访问父类的公有属性/调用共有方法
# print b.num1
# b.test()

# 在外界不能直接访问对象的私有属性/调用私有方法
# print b.__num2
# b.__test()
