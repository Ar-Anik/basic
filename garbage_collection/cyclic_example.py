import gc

class Node:
    def __init__(self):
        self.ref = None

objs = []

for _ in range(10000):
    a = Node()
    b = Node()

    a.ref = b
    b.ref = a

    objs.append((a, b))

objs.clear()

print("Before GC : ", gc.get_count())
"""
gc.get_count() = How many objects have been allocated (and not yet collected) since the last collection at 
each generation level.
"""
collected = gc.collect()
print("Garbage Collected : ", collected)
print("After GC : ", gc.get_count())

