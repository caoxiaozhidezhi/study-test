# _*_ coding:utf-8 _*_
a = 'xydz'
print("反向输出", a[::-1])

l = [2, 8, 50, 3]
print("升序排列", sorted(l))

# ===给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，
# 以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）
# 思路：1、提取keys并排序；2、map高阶函数转换字符串；3、拼接字符串
b = {1: 1, 2: 2, 3: 3}
print(",".join(map(str, sorted(b.keys()))))

# ===给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）
e = "xyzwd"
print("间隔取字", e[::2])

# ===已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开。
a = 2
b = 2
print("面积为%d 周长为%d" % (a * b, (a + b) * 2))


# ===一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
L = [0, 1, 2, 3, 4]
L.sort()
if len(L) % 2 == 0:
    print("中位数为", (L[len(L) / 2] + L[len(L) / 2 - 1]) / 2.0)
else:
    print("中位数为", L[int(len(L) / 2)])


# ===两个正整数a和b， 输出它们的最大公约数。
# 一个数除以另一个数，要是比另一个数小的话，商为0，余数就是它自己。
a = 6
b = 9
while b:
    a, b = b, a % b
    # print a, b
print("最大公约数为", a)


# ===两个正整数a和b， 输出它们的最小公倍数。
a = 6
b = 9
c = a * b
while b:
    a, b = b, a % b
print("最小公倍数为", c // a)


# 星阵
row = 1
while row <= 5:
    print("*" * row)
    row += 1
print("\n")

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1
print("\n")

# ============九九乘法表================
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print(" ")
print("\n")

for i in range(1, 10):
    for j in range(i, 10):
        print(("%d*%d=%2d") % (i, j, i * j), end=" ")
    print(" ")
print("\n")

for i in range(1, 10):
    for k in range(1, 10 - i):
        print("      ", end=" ")  # 有6个空格
    for j in range(1, i + 1):
        product = i * j
        print("%d*%d=%2d" % (i, j, product), end=" ")
    print(" ")
