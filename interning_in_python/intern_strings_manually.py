import sys

x = sys.intern("Hello World")
y = sys.intern("Hello World")

print(id(x))
print(id(y))

print(x is y)
