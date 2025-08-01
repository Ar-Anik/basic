"""
ctypes.c_long.from_address(address).value ->
This line is using Python’s ctypes module to peek into a specific memory address and read the value as a long (typically
a 64-bit signed integer on most platforms).
"""

import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

a = [1, 2, 3]
b = [4, 5, 6]

a = b
b = a

address_1 = id(a)
address_2 = id(b)

a = None
b = None

print(ref_count(address_1))
print(ref_count(address_2))
