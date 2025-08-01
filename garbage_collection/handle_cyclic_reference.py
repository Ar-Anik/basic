"""
Q : Why Cycles Are Hard for Reference Counting?
Reference counting works like this: When an object’s reference count drops to 0, Python immediately reclaims its memory.
But in a circular reference, objects reference each other, so their reference count never drops to 0, even when our
code no longer uses them.
"""
import gc
import sys

a = []
b = []
a.append(b)
b.append(a)

memory_lc_1 = id(a)
memory_lc_2 = id(b)

a = None
b = None
# Still in memory! Because a ↔ b

print("Memory Reference of a : ", sys.getrefcount(memory_lc_1))
print("Memory Reference of b : ", sys.getrefcount(memory_lc_2))
print("How many object have in Gen 0 to 2 : ", gc.get_count())

"""
Q : How Generational GC Solves Cycles ?
-> Step-1: Track Container Objects
Python tracks all objects that can reference other objects (e.g. list, dict, class instance) using the gc module’s 
generation lists. When a new object is created, it is placed in Generation 0.

-> Step-2: Trigger Garbage Collection (Threshold Exceeded)
When Python sees enough memory activity (allocations - deallocations exceeds threshold), it triggers GC.
"""
import gc
print(gc.get_threshold())  # (2000, 10, 10)
"""
If threshold exceeded:
    * Gen 0 GC runs.
    * If survivors are many → Gen 1 GC runs.
    * Eventually → Gen 2 GC runs.
    
-> Step-3: Cycle Detection via Mark-and-Sweep
Generation 2 includes the cycle detector, which solves the circular reference problem using graph traversal, 
not refcounts. The GC uses a simplified mark-and-sweep algorithm to find and break cycles, Cycle Detection 
Algorithm (in Gen 2) : 
1. Mark Phase:
    * GC traverses all objects in Gen 2.
    * It marks all objects as unreachable by default.
    * Then it walks from known root objects (like global variables, stack frames) and unmarks anything it can reach.
    * Remaining objects are still marked as unreachable → they form cycles.

2. Sweep Phase:
    * GC examines each unreachable object:
    * If its reference count > 0, but it is not reachable from outside, it’s in a cycle.
    * GC now frees these cyclically-referenced objects, even though refcount ≠ 0. This is what reference counting 
      alone cannot do!
"""

import gc

class Node:
    def __init__(self):
        self.ref = None

# Create a cycle
a = Node()
b = Node()
a.ref = b
b.ref = a

# Remove external references
a = None
b = None

# Now only internal references remain (a → b → a)

# Force full GC (Gen 2)
print("Before GC:", gc.get_count())
unreachable = gc.collect(2)
print("Unreachable objects collected:", unreachable)

"""
Finally we say, Generational GC solves circular reference problems by, Using mark-and-sweep traversal in Generation 2
Detecting unreachable object groups that form cycles Releasing them even if refcounts are non-zero.
"""