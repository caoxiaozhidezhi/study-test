# _*_ coding:utf-8 _*_
from functools import reduce

# ==利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码==
import random
tmp = ""         # 随机码的变量
for i in range(4):
    # random.randrange(start, stop, step)返回指定递增基数集合中的一个随机数，基数缺省值为1。
    n = random.randrange(0, 2)   # 成随机数1或0，用来判断下面，是生成随机数字，还是字母
    if n == 0:
        num = random.randrange(65, 91)  # 为0时候，生成大写字母
        tmp += chr(num)
    else:
        k = random.randrange(0, 10)   # 为1时候，生成数字
        tmp += str(k)
print(tmp, "\n")


# ==把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字==
# ==输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：==
def normalize(name):
    return name.capitalize()  # capitalize()用于字符串，将字符串的首字母变成大写


l1 = ['adam', 'LISA', 'barT']
l2 = list(map(normalize, l1))
print(l2, "\n")


# ==Python提供的sum()函数可以接受一个list并求和，===============
# ==请编写一个prod()函数，可以接受一个list并利用reduce()求积：==
def prod(l):
    def fn(x, y):
        return x * y
    return reduce(fn, l)


print("3*5*7=", prod([3, 5, 7]), "\n")


# ==利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：==
def str2float(s):
    s = s.split('.')  # 以小数点为分隔符，把字符串分为两部分

    def f1(x, y):  # 函数1，小数点之前的数用这个函数处理
        return x * 10 + y

    def f2(x, y):  # 函数2，小数点之后的数用这个函数处理
        return x / 10 + y

    def str2num(str):  # 函数3，用于把字符串'123'逐个变为数字
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]

    return reduce(f1, map(str2num, s[0])) + reduce(f2, list(map(str2num, s[1]))[::-1]) / 10

    # 最后一部是这个解法的精髓
    # 小数点前的数'123'，用 x * 10 + y 正常求和就能得出123，小数点之后的数'456'要怎样才能得出0.456呢？
    # 首先把字符串'456'用list(map(str2num,s[1]))转成一个列表[4,5,6]
    # 然后用[::-1]切片的方式从后往前取，列表变为[6,5,4]
    # 然后把[6,5,4]利用reduce函数放到f2函数中计算，( 6 / 10 + 5) / 10 + 4 = 4.56，得出结果4.56
    # 再除以一个10，得出0.456，到此成功把字符串'456'变成了浮点数0.456
    # 把前后结果加起来，就得到了最终解，成功把字符串'123.456'变成了浮点数123.456


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
