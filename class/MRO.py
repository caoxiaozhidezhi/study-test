# ===================MRO顺序查找法===================
#===============多继承时，查看继承顺序的方法============


class A(object):

    def test(self):
        print("A --- test方法")

    def demo(self):
        print("A --- demo方法")


class B(object):

    def test(self):
        print("B --- test方法")

    def demo(self):
        print("B --- demo方法")


class C(B, A):
    pass


c = C()
c.test()
c.demo()


print(C.__mro__)
