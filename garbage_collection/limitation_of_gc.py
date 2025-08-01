"""
After a Generation 2 garbage collection, some objects—both cyclic and non-cyclic—can still remain in memory :
-> They are unreachable BUT not collected due to __del__() methods:
CPython’s garbage collector does not immediately collect objects in cycles if they define a __del__() method,
because the order of finalization is ambiguous. When objects in a reference cycle have __del__() methods, Python
doesn't know in which order to call those __del__() methods safely. These objects go into gc.garbage.(It only
applicable for python version <= 3.4)
"""

import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print(f"{self.name} deleted")

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a

del a, b
gc.collect()  # Even generation 2 might not collect due to __del__
print(gc.garbage)  # Could show the cyclic objects   -> It only applicable for python version <= 3.4

"""
-> Cyclic objects that are still reachable:
If a cycle is part of a live object graph (i.e. it’s reachable from your program), it’s not collected. GC only 
removes unreachable objects.

-> Objects that are tracked but not collected:
Some small immutable objects (like small tuples, strings, and ints) may be interned or not tracked at all.
GC may track them anyway but skips collection if they’re known to be safe or reused.
"""

