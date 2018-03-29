# ========================定制类专题==================================

# =======================__str__和__repr__==========================


class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)

    __repr__ = __str__
s = Student('Bob', 'male', 88)
print(s)
print()


# ==========================__len__======================================

class Students(object):

    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)
ss = Students('Bob', 'Alice', 'Tim')
print(len(ss))  # 3
print()


class Fib(object):
    """
    斐波那契数列
    """

    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            print(L, a, b)
            L.append(a)
            a, b = b, a + b
        self.list = L

    def __len__(self):
        return len(self.list)

f = Fib(10)
print("最终结果：", f.list)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("列表长度：", len(f))  # 10
print()

# =============================类中的加减乘除==============


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational(object):

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)
