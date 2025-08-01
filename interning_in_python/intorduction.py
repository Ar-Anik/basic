"""
Link : https://www.geeksforgeeks.org/python/object-interning-in-python/

Link : https://medium.com/@datasciencejourney100_83560/python-interning-for-each-data-types-397b0ba70986

Q : What Is Interning in Python ?
-> Interning in Python—particularly in CPython, the default and most widely used implementation of Python is a memory
optimization technique where only one copy of a string is stored in memory when possible, especially for immutable
objects like strings. So, rather than creating multiple objects for the same string, CPython reuses an already existing
object—thus improving performance and saving memory.

Q : Where Does Interning Happen?
-> Interning happens primarily with:
    * Strings (most relevant)
    * Small integers (though not technically called "interning", it's caching, the mechanism is similar)

# Interning Strings in CPython
-> When we create two strings with the same content:
"""
a = "hello"
b = "hello"
"""
Instead of storing "hello" twice in memory, Python may store it once and point both a and b to the 
same memory location. That means:
"""
print(a is b)  # True in many cases due to interning
print(a == b)  # Always True, since values are same
"""
a == b checks value equality. a is b checks whether both point to the same object.
If interning occurred, a is b will be True.
"""

"""
Q : When Does CPython Automatically Intern Strings?
1. Identifiers : Strings that are valid variable/function/class names (i.e., match identifier syntax rules). These are 
used frequently in the interpreter and source code, so CPython interns them for performance. it's talking about the 
string values that look like valid identifiers — for example:
    s1 = "count"
    s2 = "user_data"
    s3 = "for"
    s4 = "class"

These are strings that look like variable names, and CPython detects that they're shaped like identifiers.
Since such strings are very commonly used — especially internally for:
    * Variable names
    * Function names
    * Class names
    * Keywords (if, for, while)

CPython may automatically intern these strings for memory efficiency and fast identity comparison

2. Short Strings : If we use short strings (like "hello", "yes", "abc123"), Python may store only one copy of 
them in memory. This happens automatically when Python compiles our code (before running it). So if the same 
short string appears multiple times, Python will reuse the same object instead of creating new ones.

3. String Literals from Source Code : A string literal is any string we write directly in our Python code using 
quotes: a = "hello"  # ← this is a string literal
When Python compiles our code (before it runs), it may detect that some of these strings are:
    * Short
    * Alphanumeric (no special characters or spaces)
    * Repeated multiple times
If that’s the case, Python will intern them — meaning it will store only one copy in memory and reuse it.
String that is Long or have special characters, it not interned automatically

4. Strings with Only Letters, Digits, and Underscores : Alphanumeric strings (a–z, A–Z, 0–9, _) with no whitespace or 
special characters are good candidates for interning. Example : "abc123", "user_name"
"""

"""
Q : When Is a String Not Interned?
-> If a string:
    * Is created at runtime (e.g., through input, join, concatenation, slicing)
Then Python may not intern it automatically.
"""

x = "hello i am @nik, from bangladesh, wh!te house, dhaka-1200, but i from bangladesh123"
y = "hello i am @nik, from bangladesh, wh!te house, dhaka-1200, but i from bangladesh123"
print(x is y)

"""
Q : Why Interning Matters?
1. Memory Optimization
Avoids storing many copies of the same string in memory. If we're processing a dataset with lots of repeated 
strings (e.g., "yes", "no", "unknown"), interning saves memory.

2. Faster Comparisons
When strings are interned, a is b is faster than a == b, because it's comparing memory addresses, not content.
This is important when doing millions of comparisons (like in parsers, compilers, symbol tables, etc.).
"""

first = "a" * 1000
second = "a" * 1000
print(first is second)

first_int = 12345678901234567890
second_int = 12345678901234567890
print(first_int is second_int)

a = (1, 2, "hello")
b = (1, 2, "hello")
print(a is b)
print(a[2] is b[2])

a = 2.45
b = 2.45
print("Float : ", a is b)

a = True
b = True
print("Boolian : ", a is b)

"""
-> Only immutable types interned. Mutable types are never interned.

Interning means reusing the same object in memory for performance (like saving memory or speeding up comparison).
Mutable objects (like lists or dicts) can change after creation, so sharing them across different variables would 
be unsafe. Immutable objects (like strings, integers, tuples) are safe to reuse, because they can't be modified in-place.

Immutable : integer, float, boolian, string, tuple etc.
Mutable : list, dictionary, set etc.
"""

# List
a = [1, 2, 3]
b = [1, 2, 3]
print("List : ", a is b)

# Set
a = {1, 2, 3}
b = {1, 2, 3}
print("Set : ", a is b)

# Dictionary
a = {"key": "value"}
b = {"key": "value"}
print("Dictionary : ", a is b)

