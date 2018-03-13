# _*_ coding:utf-8 _*_
print("类的例子:")


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


# ===把Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：=========
print("\n")
print("访问限制——私有变量:")


class Student1(object):

    def __init__(self, name, gender):
        # 构造方法
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        # 外部代码获取gender
        return self.__gender

    def set_gender(self, gender):
        # 外部代码修改或者判断gender
        if gender == "male" or "female":
            self.__gender = gender
        else:
            raise ValueError('bad gender')


# 创建实例对象
bart = Student1('Bart', 'male')

print(bart.get_gender())

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

# ====================继承和多态======================
print("\n")
print("继承和多态:")


class Person(object):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")


class Child(Person):                            # Child 继承 Person
    pass


May = Child("May", "female")
Peter = Person("Peter", "male")

print(May.name, May.sex, Peter.name, Peter.sex)    # 子类继承父类方法及属性
May.print_title()
Peter.print_title()


# ===为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：===
print("\n")
print("统计学生：")


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    print("当前学生数：", Student.count)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
print(bart.name, lisa.name, Student.count, "\n")


# =======================使用__slots__===============
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
