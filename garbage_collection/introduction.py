"""
Link : https://www.geeksforgeeks.org/python/garbage-collection-python/

-> Garbage Collection in Python is an automatic memory management process that monitors objects in our program and frees
memory used by objects that are no longer in use (i.e., no variable or data structure is referencing them).

Instead of requiring us to manually release memory (as in languages like C/C++), Python's garbage collector automatically
reclaims memory, meaning it detects and deletes unused objects without any explicit instruction from the programmer.
This helps prevent memory leaks and keeps memory usage efficient.
"""

"""
Q : What is a Circular Reference?
-> A circular reference occurs when two or more objects reference each other, directly or indirectly, forming a loop.

Circular references prevent memory from being freed in reference counting systems because each object in the cycle 
keeps the other alive, even if they are no longer accessible from our program.

Reference counting only deletes an object if its count is 0. In a circular reference, each object has at least 1 
reference (from the other). So their count is never 0, and memory is not released, even though we can't access 
them anymore.
"""

# circular reference
import ctypes

a = [1, 2, 3]
b = [2, 3, 4]

a.append(b)
b.append(a)

print(a)
print(b)

memory_address_1 = id(a)
memory_address_2 = id(b)

a = None
b = None

print(a)
print(b)

print(ctypes.c_long.from_address(memory_address_1).value)
print(ctypes.c_long.from_address(memory_address_2).value)

"""
Here, a point b and b point a. Each one increased the reference count of the other. This forms a cycle: each list is 
keeping the other alive. When we write a = None and b = None. This removes our names a and b from the current namespace.
That means a and b now not point there list in memory. But the lists themselves still exist in memory, because:
    * a still existed inside b
    * b still existed inside a
So their internal reference counts didn’t drop to 0.

-> Python uses a cycle detection algorithm built into the gc module (Garbage Collector) to find and clean up circular 
references that reference counting alone can't collect.
"""

"""
-> For memory management Python uses:
    * Reference Counting (fast, immediate collection)
    * Cycle Detector (GC module) for cleaning up cycles
Python’s GC algorithm is:
    * Generational
    * Tracking
    * Non-recursive mark-and-sweep

-> The GC only tracks container objects that can hold references: list, dict, tuple, set, class instances etc.
Not simple objects like int, str, float (they can’t cause cycles).
"""

