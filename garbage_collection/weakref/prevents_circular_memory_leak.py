import gc
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __del__(self):
        print(f"Deleted {self.name}")

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
"""
gc.get_debug(gc.DEBUG_UNCOLLECTABLE : This line enables debug logging for Python’s garbage collector (GC), specifically 
to show information about uncollectable objects — i.e., objects that:
    * Are involved in circular references, and
    * Cannot be safely deleted, so
    * Are put into the special list gc.garbage.
Then when we write : gc.collect()
If there are any unreachable objects that could not be safely deleted, Python prints debug info like:
    gc: collectable <__main__.Node instance at 0x...>
    gc: uncollectable <__main__.Node instance at 0x...>
"""

x = Node("X")
y = Node("Y")

x.partner = y
y.partner = x

x = None
y = None

unreachable = gc.collect()

print("Unreachable collected:", unreachable)
print("gc.garbage length   :", len(gc.garbage))

# use weakref
a = Node("A")
b = Node("B")

a.partner = weakref.ref(b)
b.partner = weakref.ref(a)

a = None
b = None

unreachable = gc.collect()

print("Unreachable collected:", unreachable)
print("gc.garbage length   :", len(gc.garbage))
