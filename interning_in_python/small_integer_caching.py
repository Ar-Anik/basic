"""
--> For small integers, Python (specifically CPython) uses integer object caching, not interning. The term “interning”
is used for strings. For integers, Python pre-creates objects and reuses them, that’s called caching.
So, String interning and Integer caching.

--> When the interpreter starts, it creates a fixed pool of integer objects — by default, for integers in the range:
    -5 to 256
Any time we create an integer in that range, Python reuses the same object, instead of allocating new memory. To
optimize performance and memory usage. These small numbers are used all the time — in loops, indexing, booleans, etc.

--> At interpreter startup. The small integer cache is initialized before any of our code runs, during CPython’s
internal init process. CPython keeps small integers in a hidden array. In CPython source code:
/* Objects/intobject.c */
static PyObject *small_ints[NSMALLPOSINTS];  // usually NSMALLPOSINTS = 257

// Initialized at interpreter startup:
for (i = 0; i < NSMALLPOSINTS; i++) {
    small_ints[i] = PyInt_FromLong(i - 5);
}
So Python literally allocates and stores in memory at startup : [-5, -4, ..., 256]
"""

a = 100
b = 100
print(a is b)

memory_address = id(a)

import sys
print(sys.getrefcount(a))

# Part-1
x = 1000
y = 1000

print(x is y)

# Part-2
c = int("1000")
d = int("1000")

print(c is d)

"""
Here, x is y return True because of constant folding during bytecode generation.

Q : What is Constant Folding?
-> Constant folding is a compiler optimization where Python evaluates constant expressions at compile time, instead of 
at runtime. This reduces runtime computation by replacing expressions like 2 + 3 with 5 during bytecode generation.

# Example:
-> Without Constant Folding: x = 2 + 3
Normally, this would mean: Add 2 + 3 at runtime. Then assign to x

-> With Constant Folding: Python sees that 2 and 3 are both constants. It computes 5 at compile time, and stores x = 5 directly.

-> Part 1: Static Constants — Reused via Constant Folding
At compile time, Python sees 1000 written twice. It folds them into a single constant in the bytecode.(When Python 
sees multiple identical constants (like 1000, "hello", 3.14, etc.) written in source code, the Python compiler 
doesn't store them multiple times. Instead, it creates just one object, and reuses it wherever needed.)
Both x and y are assigned to the same object. So, x is y return True (in some cases).

-> Part 2: Dynamic Construction — New Objects Every Time
int("1000") creates a new integer object at runtime. Python cannot know "1000" ahead of time (could be from user input).
So x and y point to different objects. x is y return False.
"""

