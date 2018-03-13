# _*_ coding:utf-8 _*_
import time
import datetime
import functools
# ============装饰器示例============


def log(func):
    def wrapper(*args, **kwargs):
        print("log")
        temp = func(*args, **kwargs)
        return temp
    return wrapper


# 运行时间
def my_time(func):
    def wrapper(*args, **kwargs):
        print("time")
        temp = func(*args, **kwargs)
        return temp
    return wrapper


@log
@my_time  # => f = my_time(f)
def f(x):
    return x


n = f("i am x")
print("n = ", n, "\n")


# ====请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：===
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print("%s executed in %s ms" % (func.__name__, end - start))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
