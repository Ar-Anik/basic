"""
Before read reference counting must be konw python interns.

Link : https://medium.com/@jayantnehra18/python-fundamentals-reference-counting-25cea69cd6ae

Q : What is Reference Counting?
-> Reference counting is a mechanism that keeps track of the number of references (names or variables) that point to
a particular object in memory. Python manages memory automatically. We don't manually allocate or free memory. Python
uses reference counting to know when it can safely delete an object.

Q : What Happens in CPython When We Write: x = 1000 ?
Step 1: Check if the integer 10000 is already interned (cached)
CPython interns (caches) small integers from -5 to 256. These are pre-created and reused for efficiency. Since 10000
is outside this range, it is not interned.

Step 2: Create a new integer object
Python creates a new int object to represent 10000. In memory, this object has:
    * Type info (int)
    * Value (10000)
    * Reference count = 1 (initial, because it's now referenced by the assignment)

Step 3: Assign the new object to variable a
The variable name a in the current namespace (like locals or globals) is now bound to this int object. Binding a to
this object increments the reference count by 1. Now RefCount(10000) = 2.  One reference from internal temporary use
in the evaluation. One reference from the name a. (Actually, the temporary reference used by the bytecode interpreter
disappears right after the assignment, so it's really just 1 at rest.)

Step 4: Clean-up of Temporary References
CPython removes temporary references created during evaluation.
After cleanup: RefCount(10000) = 1, This 1 reference is from the variable a.
"""


"""
Q : How Reference Counting Works Internally in Python?
-> Reference Counting is a memory management technique used by CPython (the standard Python interpreter) to keep track 
of the number of active references to each object in memory. When an object's reference count drops to zero, it means 
no one is using it anymore—so Python automatically deallocates (frees) that object’s memory.

-> Internal Working of Reference Counting : 
Step-1: Object Creation
When we create a new object in Python: x = 20000
Internally, CPython creates an object that (conceptually) still includes:
    * A reference count
    * A pointer to its type info
    * Possibly other fields (value, size, etc.)
In Python 3.12+, the reference count field is no longer directly visible as ob_refcnt. Instead, it's accessed via 
macros or inline functions like:
    * Py_REFCNT(obj)
    * Py_INCREF(obj)
    * Py_DECREF(obj)

Step-2: Reference is Added (Increment Count)
Every time a new reference is created: y = x  (Now both x and y point to the same object)
CPython calls: Py_INCREF(obj);
This increments the reference count atomically under the hood.

Step-3: Reference is Removed (Decrement Count)
When a reference is deleted or reassigned: del x
CPython calls: Py_DECREF(obj);
Which Decreases the reference count by 1. If the count drops to 0, the object is deallocated. This deallocation 
involves:
    * Calling the object’s tp_dealloc() function.
    * Releasing memory via PyObject_Free().
    
Step-4: Reference Count Lookup (Debugging)
We can still inspect reference count from Python using:
"""
import sys
x = 1000
print(sys.getrefcount(x))
"""
Internally this calls: Py_REFCNT(obj)

-> Disadvantages of Reference Counting
1. Cannot Handle Cyclic References
2. Overhead in High-Frequency Operations
    * Every time a reference is added or removed (even in tight loops), the reference count must be updated.
    * In multi-threaded environments, this means atomic operations or locks, which can slow down performance.
3. Harder to Optimize with Multiple Threads (GIL)
    * To avoid memory corruption, reference counting requires the Global Interpreter Lock (GIL) in CPython.
    * The GIL prevents multiple threads from executing Python bytecode simultaneously.
4. Extra Bookkeeping for Each Object
Every object must store a reference count, which adds memory overhead—especially for small objects (like 
integers or small strings).
"""
