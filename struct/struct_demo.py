# https://docs.python.org/3/library/struct.html
from struct import *

p = pack(">bhl", 1, 2, 3)
print(p, type(p))
# up = unpack('>bhl', b'\x01\x00\x02\x00\x00\x00\x03')
up = unpack('>bhl', p)
print(up, type(up))

c = calcsize('>bhl')
print(c, type(c))

# pack(">b", 99999)
# pack(">h", 99999)
print(pack(">l", 99999))
print(unpack(">l", pack(">l", 99999)))


def print_calcsize(x):
    print(f"{x} size: {calcsize(x)}")


print_calcsize('>x')
print_calcsize('>c')
print_calcsize('>b')
print_calcsize('>B')
print_calcsize('>?')
print_calcsize('>h')
print_calcsize('>H')
print_calcsize('>i')
print_calcsize('>I')
print_calcsize('>l')
print_calcsize('>L')
print_calcsize('>q')
print_calcsize('>Q')
# print_calcsize('>n')
# print_calcsize('>N')
print_calcsize('>e')
print_calcsize('>f')
print_calcsize('>d')
print_calcsize('>s')
print_calcsize('>p')
# print_calcsize('>P')
print_calcsize('@ccc')
print_calcsize('@3s')
print_calcsize('@ci')
print_calcsize('@ic')

# ---------------------------------------------------------- #

print(pack('f', 1.73))
print(unpack('f', pack('f', 1.73)))

s = pack('f', 1.73) + pack('i', 1)
print(f"s: {s}")
f = unpack('f', s[0:4])
print(f"f: {f[0]}")
i = unpack('i', s[4::])
print(f"i: {i[0]}")

print(f"unpack s: {unpack('fi', s)}")

# ---------------------------------------------------------- #
record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)
print(name, serialnum, school, gradelevel)

from collections import namedtuple

Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(unpack('<10sHHb', record))
print(unpack('<10sHHb', record), type(unpack('<10sHHb', record)))
print(Student, type(Student))
print(Student.name, type(Student.name))
print(Student.serialnum)
print(Student.school)
print(Student.gradelevel)
print("-"*120)
# 必须实例化才行
student = Student._make(unpack('<10sHHb', record))
print(student)
print(student.name, type(student.name))
print(student.serialnum)
print(student.school)
print(student.gradelevel)

# https://www.cnblogs.com/coderzh/archive/2008/05/04/1181462.html
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017685387246080
