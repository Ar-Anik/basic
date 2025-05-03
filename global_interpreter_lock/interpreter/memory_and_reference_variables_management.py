"""
-> Python interpreter (CPython) manages memory and reference variables using a combination of:
    * Reference counting (primary method),
    * Garbage collection (for cycles),
    * Memory allocators (to request/release memory from the OS).
"""

"""
Q : What Is a "Reference Variable" in Python?
Step-1 : In Python, x = [1, 2, 3]

Here:
    * x is not the list itself.
    * It’s a reference (a pointer) to the list object in memory.

Every object (list, int, str, etc.) lives somewhere in memory.
All variables are just references to those objects.

So when we do, y = x now we have two references to the same object.

Step-2 : Reference Count
Every object in Python has a hidden reference count. It's an integer that tracks: "How many variables point to me?"
Example:
    x = [1, 2, 3]
    y = x
    z = x

x, y, and z all point to the same list. So the list’s reference count is 3.

When one of the variables is deleted: del x
The reference count becomes 2.

When the reference count reaches 0, the object is no longer needed, and the memory is freed.

Step-3: How Reference Counting Works Internally
Every Python object is actually a C structure (PyObject) that looks like this:
    typedef struct {
        Py_ssize_t ob_refcnt;  // <== THIS is the reference count
        struct _typeobject *ob_type;  // pointer to type info
    } PyObject;

When we do x = [1, 2, 3]:
    * Python creates a PyObject for the list.
    * Sets the reference count to 1.
    * Every time another variable points to it, the ref count is increased.

When x = None or del x: Python calls Py_DECREF(obj) which decreases the reference count.
If ref count hits 0, Python automatically deallocates the memory for that object.

Q : Why This Needs the GIL
All threads share memory and objects. So, when multiple threads are increasing/decreasing reference counts 
(which is just a number in memory), we need a lock — otherwise:
    * Thread A might increase it at the same time Thread B decreases it.
    * This creates a race condition — memory may be freed while it’s still in use.
The GIL ensures only one thread at a time modifies reference counts or memory.
"""

import sys
a = [1, 2, 3]
b = a
print("Reference : ", sys.getrefcount(a))

"""
-> Garbage Collector for Cycles : Reference counting cannot handle cycles.
Example :
    a = {}
    b = {}
    a['b'] = b
    b['a'] = a
Both a and b reference each other. Even after del a and del b, their internal links keep their reference counts above 0.
So Python uses a cyclic garbage collector:
    * Scans objects to find reference cycles.
    * Breaks the cycles if no external references exist.
    * Frees memory.
The cyclic GC works in the background and is triggered periodically.
"""

a = {'x': 1, 'y': 2}
b = {'y': 1, 'x': 2}

a['b'] = b
b['a'] = a

del a

print("Reference count of b['a']:", sys.getrefcount(b['a']))

"""
--> Memory Management System (pymalloc)
CPython uses its own memory manager:
    * Small objects (less than 512 bytes) are allocated using pymalloc.
    * It avoids calling the OS each time to make things faster.
    * Python keeps memory "arenas" to reuse space.
-> Large objects (like big strings or lists) may directly use malloc from the C library.

"""