# -*- coding: utf-8 -*-
from functools import reduce

a = {1: 1, 2: 2, 3: 3}
print(",".join(map(str, sorted(a.keys()))))

b = "xyzwd"
print(b[::2])

l = []
i = 0
while i < len(b):
    if i % 2 == 0:
        l.append(b[i])
    i += 1
print("".join(l), "\n")


# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst)
    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print(f)
print(f())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
