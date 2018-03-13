# _*_ coding:utf-8 _*_

# ========利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：==========


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == " ":
        return trim(s[1:])
    elif s[-1] == " ":
        return trim(s[:-1])
    return s


print(trim("hello "))
print(trim(" hello"))
print(trim(" hello "))
print(trim(""))
print(trim("  "))


# =====请使用迭代查找一个list中最小和最大值，并返回一个tuple：=====
print("==========分割===============")


def findMinAndMax(L):
    if not bool(L):
        return (None, None)
    min = max = L[0]
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
print(findMinAndMax([7, 1, 3, 9, 5]), "\n")


# ==================列表生成式========================
print("==========分割===============")
l1 = ["Hello", "World", 18, "Apple", None]
l2 = [s.lower() for s in l1 if isinstance(s, str)]
print(l2)
if l2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
