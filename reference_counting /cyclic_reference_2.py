import sys

a = [1, 2, 3]

print(sys.getrefcount(a))
a.append(a)

print(a[0])
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])
print(a[3][3])

print(sys.getrefcount(a))
a.append([8])
print(a)
print(a[4])

print(sys.getrefcount(a))
b = a
a = None

print(sys.getrefcount(b))
