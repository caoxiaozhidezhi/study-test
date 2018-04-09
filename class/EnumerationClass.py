# ======================枚举类专题=====================

from enum import Enum

myMonth = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May",
                         "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

for name, member in myMonth.__members__.items():
    print(name, ',', member, ',', member.value)

l = list(myMonth.__members__.items())

print(myMonth.Jan)
print(myMonth.Jan.value)
print(l)
print(l[0], type(l[1]), l[0][1], type(l[0][1]))
