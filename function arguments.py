# _*_ coding:utf-8 _*_
# ========================函数参数专题======================
import math

# =======================一元二次方程求解===================
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0的两个解。


def quadratic(a, b, c):
    for n in (a, b, c):
        # 判断参数类型：isinstance()函数用来判断一个对象是否是一个已知的类型
        # 判断n是否为int或float类型
        if not isinstance(n, (int, float)):
            # 异常处理
            raise TypeError('Wrong operand type')

    delta = b**2 - 4 * a * c

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    else:
        print('原方程无解')


print(quadratic(2, 3, 1), "\n")


# =========================参数组合=========================

def f1(a, b, c=0, *args, **kw):
    print("a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, "a", "b")
f1(1, 2, 3, "a", "b", x=99)
print("\n")


# =============================实例应用=========================
# 假设传入一个班级的名字、班级所获荣誉，以及各位任课老师的名字和年龄
def welcome(name, *args, **kw):  # name为必选参数，*args为可变参数，**kw为关键字参数
    print("%s共获得了%d项荣誉，分别是：" % (name, len(args)))
    for i in range(len(args)):
        print("%d.%s" % (i + 1, args[i]))

    age_sum = 0
    print("该班共有%d名老师，他们的名字和年龄如下：" % len(kw))
    for value in kw:
        age_sum += kw[value]
        print("%s:%d岁" % (value, kw[value]))
    print("老师们的平均年龄是%.1f岁n" % (age_sum / len(kw)))


welcome('计算机1班', '校优秀班级', '最佳凝聚力', Mary=27, Peter=35, John=32)
welcome('软件2班', '上海市优秀班级', '校合唱比赛冠军', '最佳凝聚力',
        Peter=34, Rose=28, Hans=33)
print("\n")
