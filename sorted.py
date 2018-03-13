# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 按名字排序
def by_name(t):
    return t[0]


# 成绩由高到低排序
def by_score(t):
    return (-t[1])


L1 = sorted(L, key=by_score)
L2 = sorted(L, key=by_name)
print(L1)
print(L2)
