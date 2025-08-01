"""
1. Equality operator (==) : Compares values (contents)

2. Identity operator (is) : Compares memory addresses (object identity)
"""

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

"""
a and b are two separate objects in memory But their contents are equal
"""

print(a is b)

"""
Even though a and b look the same, they were created separately, so they live at different memory locations.
"""

# Python interned the string
x = "hello world"
y = "hello world"

print(x == y)       # True – same value
print(x is y)       # True – same object (likely interned)


#  Integers (small vs large)
c = 100
d = 100
print(c is d)   # True – small integers are cached


e = 12456783976
f = 12456783976

print(e is f)

memory_address_i = id(e)
memory_address_f = id(f)

print(memory_address_i, " ------ ", memory_address_f)

import ctypes
import sys
print(ctypes.c_long.from_address(memory_address_i).value)

print(sys.getrefcount(e))

"""
Literal Value : A literal is a value that we write directly in our code, not calculated or returned by a function or expression.

-> e is f, print True. Because both e and f are assigned the same exact large literal value, and that value appears 
only once in the compiled bytecode, CPython optimizes it like this:
-> At Compile Time:
    * Python sees the exact same literal twice.
    * It stores one constant value in the compiled .pyc bytecode.
    * Both e and f are set to the same reference of that constant object.
It’s not integer caching. It’s compile-time constant folding + literal deduplication.
"""

g = int("12456783976")
h = int("12456783976")

print(g == h)
print(g is h)

