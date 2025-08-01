"""
Link : https://www.geeksforgeeks.org/python/garbage-collection-python/

Q : What is Generational Garbage Collection?
-> Generational Garbage Collection is a memory management optimization technique used by Python's garbage collector to
improve efficiency by grouping objects based on their age (how long they have lived).

-> Generational Garbage Collection is a memory management technique used by Python (CPython) where objects are grouped
into generations based on their age, and younger generations are collected more frequently than older ones.

-> Python’s generational garbage collector (used in CPython) only cleans up cyclic garbage — that is, unreachable objects
involved in reference cycles that the reference counting system cannot handle on its own. Its only job is to:
        Detect and collect cyclic garbage that reference counting can’t free.

-> GC does NOT run for non-cyclic objects. GC only runs to detect unreachable cyclic structures.

Q : Why Generational GC?
-> Observation (Empirical Fact): Most objects in programs die young — meaning they become unreachable and can be freed
soon after being created. A few objects live longer (like global configs, database connections).

-> Goal: Avoid scanning the entire heap for garbage on every GC run. Instead, focus on young objects more frequently
because they are more likely to be garbage. Python divides objects into three generations and focuses on the youngest
first.

Q : How Python implements this idea?
    1. Objects are organized into 3 generations (0, 1, 2).
    2. New objects start in Generation 0.
    3. Objects that survive garbage collection in Gen 0 are promoted to Gen 1.
    4. Objects that survive further collections in Gen 1 are promoted to Gen 2.
    5. Generation 2 objects are collected less often because they tend to live longer.

-> Generations in Detail
Gen 0 : Newly created objects. --> Collected most frequently (every time GC runs) --> Dead objects are removed, survivors go to Gen 1
Gen 1 : Objects that survived one or more Gen 0 GCs. --> Collected less frequently --> Survivors move to Gen 2
Gen 2 : Objects that survived multiple collections, considered long-lived. --> Collected rarely (full GC) --> Full scan of all tracked objects


Q : How Generational Garbage Collection Works ?
-> Step-1: Object Creation
Every new object (e.g., list, dict, class instance) is placed in Generation 0. like : a = [1, 2, 3]  # a goes to Gen 0

-> Step-2: Threshold-Based Trigger
Python tracks how many allocations - deallocations happen. When the number of allocations minus deallocations exceeds
a threshold for Gen 0, Python triggers collection on Gen 0. Same for Gen 1 and Gen 2. After collection if Gen 0 still
has survivors, they’re promoted to Gen 1.
"""

import gc
print(gc.get_threshold())   # show result (2000, 10, 10)

"""
This means:
-> After 2000 new objects (net), Gen 0 is collected. If Gen 0 still has survivors, they’re promoted to Gen 1.
-> 10 Threshold for Generation 1
-> 10 Threshold for Generation 2

-> Step-3: Collection of Gen 0
Python collects Gen 0: Unreachable objects in Gen 0 are destroyed. Survivors are promoted to Gen 1.
Gen 0
│
├─ [short-lived objects] → collected
└─ [survivors] → promoted to Gen 1

-> Step-4: Collection of Gen 1
If many objects survive Gen 0 collection, it might trigger Gen 1 collection. Gen 1 collection Happens less 
frequently. Scans all Gen 0 and Gen 1 objects. Surviving Gen 1 objects are promoted to Gen 2.
Gen 1
│
├─ [dead objects] → destroyed
└─ [survivors] → promoted to Gen 2

-> Step 5: Collection of Gen 2 (Full GC)
Again if many objects survive Gen 1 collection, it might trigger Gen 2 collection. Gen 2 Collection least 
frequent and most expensive. It scans all generations (Gen 0 + Gen 1 + Gen 2). so Python avoids it unless 
necessary. It cleans up any remaining garbage, including cyclic references.


Q : Why This Works Efficiently ?
-> Because most objects die young, frequent Gen 0 collections clean up many objects quickly, avoiding 
expensive full-heap scans. Older objects are scanned less often, saving CPU time. This approach balances 
speed and memory cleanup effectiveness.
"""

print(gc.get_count())      # (45, 5, 0)

"""
Returns how many objects are currently in:
    * Gen 0 (45)
    * Gen 1 (5)
    * Gen 2 (0)
"""

# Set new thresholds: (gen0_threshold, gen1_threshold, gen2_threshold)
gc.set_threshold(50, 5, 5)
print(gc.get_threshold())

"""
The collector runs for Gen 0 when allocations - deallocations > gen0_threshold. Gen 1 and Gen 2 thresholds 
work similarly but for their respective generations.
"""

# Manually trigger collection
gc.collect(0)       # Collect only Gen 0
print(gc.get_count())
gc.collect(1)       # Collect Gen 0 + Gen 1
print(gc.get_count())
gc.collect(2)       # Full GC (all generations)
print(gc.get_count())

