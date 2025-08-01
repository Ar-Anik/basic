import gc

print("Initial Thresholds : ", gc.get_threshold())
print("Current Counts : ", gc.get_count())

# create many short-lived objects
for _ in range(10000):
    a = [1, 2, 3, 4]

print("Counts  after allocations : ", gc.get_count())

# Full Collection
collected = gc.collect()
print(f"Garbage Collected objects : {collected}")

print("After Collected : ", gc.get_count())

"""
Here, Garbage Collected objects : 0
Even after allocating many objects because those objects are not garbage.

Each time through the loop, we're creating a new list object and assigning it to a. The previous list 
assigned to `a` is immediately eligible for collection (reference goes away), but it doesn’t form any 
reference cycles. So after each iteration, the old list becomes unreachable but not tracked as garbage. 
Python relies on reference counting primarily, and these objects are cleaned up immediately by the 
reference counter itself — not deferred to the garbage collector (GC).

-> Reference Counting cleans it up immediately : a = [1, 2, 3, 4]
This list has a reference count of 1. When the next iteration runs, a is reassigned, and the reference 
to the previous list drops to 0. So, CPython immediately destroys the previous list. Garbage collector 
isn’t involved.

-> Garbage Collector only handles cyclic references
Python's gc module is only for cyclic garbage — objects that reference each other and can’t be cleaned 
up by reference counting alone. Our [1, 2, 3, 4] lists don’t have any self-references or cycles, so they 
are cleaned up without needing GC.

-> Why gc.collect() returns 0
Because there’s nothing left for the GC to collect. gc.collect() only collects unreachable objects that 
are part of a reference cycle. Since there are no such cycles created in our code, it returns 0.
"""