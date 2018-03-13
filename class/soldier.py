# _*_ coding:utf-8 _*_

"""
重点：一个对象的属性，可以是另一个类创建的对象（例如本代码中的枪类，可以在士兵类中创建）
需求：
1、士兵许三多有一把AK47
2、士兵可以开火
3、枪能够发射子弹
4、枪装填子弹--层架子弹数量
"""


class Gun:
    """枪类"""

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数
        self.bullet_count = 0

    def add_bullet(self, count):
        # 加子弹
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("【%s】没有子弹了..." % self.model)
            return
        # 发射子弹，-1
        self.bullet_count -= 1
        # 提示发射信息
        print("【%s】突突突...[剩余子弹：%d]" % (self.model, self.bullet_count))


class Soldier:
    """士兵类"""

    def __init__(self, name):
        self.name = name

        # 新兵没有枪(设置为空对象)
        self.gun = None

    def fire(self):

        # 判断士兵是否有枪（使用身份运算符is 或者is not）
        # is和==的区别是，is用来判断内存地址是否一样，==用来判断变量值是否一样
        if self.gun is None:
            print("[%s]还没有枪..." % self.name)
            return
        # 高喊口号
        print("冲啊...[%s]" % self.name)
        # 让枪装填子弹
        self.gun.add_bullet(50)
        # 让枪发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")
# 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
