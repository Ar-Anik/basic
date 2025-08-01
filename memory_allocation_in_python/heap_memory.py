"""
Heap Memory is the region of memory where dynamically allocated objects are stored—like:
    * objects (list, dict, set, class instances, etc.),
    * functions,
    * closures,
    * and other non-primitive types that live beyond function calls.

> Memory Layout in CPython (Simplified)
Here's a simplified view of how memory is organized in CPython:
    +-----------------------------+
    | Code & Static Data         | ← .text / .data
    +-----------------------------+
    | Stack Memory               | ← Function call frames
    +-----------------------------+
    | Heap Memory                | ← All Python objects live here
    +-----------------------------+
    | OS Kernel Memory           |
    +-----------------------------+

-> How Heap Memory Works in Python
1. Interpreter Startup — Python Allocators Get Ready
When we run a Python program, CPython sets up several memory allocators:
> OS Allocator
Q : What is it?
Functions like malloc(), calloc(), and free() provided by the Operating System (OS).

Q : Why it's needed?
Python still needs the OS to request physical memory from RAM. Only the OS can actually allocate raw memory to a process.

Q : Why not use only this?
Calling malloc() and free() frequently is:
    * Slow
    * Fragmented
    * Costly in system calls
    * Not specialized for small Python objects (e.g., many tiny lists or ints)

This is the foundation layer. All other allocators rely on this to actually get memory from the system.

> Python Raw Allocator
Q : What is it?
A thin wrapper around malloc() / free(), named:
    * PyMem_RawMalloc()
    * PyMem_RawFree()

Q : Why it's needed?
Some parts of Python (like interpreter startup, debugging, or C extensions) need raw memory, but:
    * Not tied to Python objects
    * Don't want full garbage collection or tracking

Q : Why not skip this?
    * Gives CPython control and customization over basic memory without being too low-level.
    * Allows Python to be ported or debugged easier (e.g., replace malloc() with a custom allocator for testing).

It gives a clean interface to raw memory, helping Python manage memory more portably and flexibly.

> Python Object Allocator (PyObject_Malloc)
Q : What is it?
A smart allocator just for Python objects. Uses small memory blocks, pools, and fast reuse.
            void *PyObject_Malloc(size_t size);

Q : Why it's needed?
Most Python objects are small (8–512 bytes). Regular malloc() is too slow and wasteful for this. PyObject_Malloc:
    * Pre-allocates memory
    * Groups same-size objects
    * Reuses freed memory
    * Avoids fragmentation
It makes Python fast and memory-efficient for real-world usage (many small objects created/destroyed constantly).

> Arena Allocator
Q : What is it?
    * Top-level allocator that grabs big 256 KB chunks (called arenas) from the OS
    * Each arena contains many pools (4 KB each), each pool has blocks for objects

Q : Why it's needed?
OS malloc() is too expensive to call for every 32-byte object. Arena allocator:
    * Gets memory from OS less frequently
    * Divides memory neatly into pools/blocks
    * Enables reuse and grouping by size
Helps batch memory requests to OS, avoiding fragmentation and system call overhead.

OS Allocator, Python Raw Allocator, Python Object Allocator (PyObject_Malloc) and Arena Allocator all are need because
small Python objects are allocated frequently and released dynamically. So CPython has its own layers on top of malloc()
for performance and fragmentation reduction.


2. Object Creation — Allocation Happens on Heap
When we write code like: x = [1, 2, 3], Here’s what happens step-by-step:

> x = [1, 2, 3] is interpreted
Python parses it, recognizes it's a list creation.

> Memory is allocated on the heap
Each object here is stored on the heap:
    * x → refers to a heap-allocated list
    * Internally, that list refers to three heap-allocated int objects (1, 2, 3)

> A pointer is stored in the local scope
The local variable x on the stack holds a pointer to the list object on the heap.

    Stack Frame of current function:
    x ───▶ (List Object in Heap)
              ├──▶ Int 1
              ├──▶ Int 2
              └──▶ Int 3

3. Memory Management: Reference Counting + GC
All objects in the heap are managed using:
    * Reference Counting (refcount)
    * Generational Garbage Collector for unreachable cycles
Objects are freed from heap only when refcount == 0

4. Heap Fragmentation & Python Object Pools
To improve performance, CPython uses object pools:

> Arenas : Large blocks (256 KB) from OS using `malloc()`
> Pools : Small blocks (~4KB) carved from arenas
> Blocks : Individual object-sized memory chunks inside pools

> Flow:
    * Arena allocated from OS (256 KB)
    * Pools divide the arena into smaller units
    * Blocks hold actual Python objects

    This helps:
        * Reuse memory blocks for same-size objects
        * Avoid heap fragmentation
        * Reduce OS memory calls

5. Heap Objects Have Lifespan Beyond Function Scope
Unlike stack memory, which is cleaned up after a function returns, heap memory:
    * Stays allocated as long as references exist
    * Gets cleaned only by GC or when refcount = 0

6. Heap vs Stack in Action
"""
def foo():
    a = [1, 2, 3]  # 'a' is a local variable (stack)
    return a       # But [1, 2, 3] list is on heap

x = foo()
"""
a lives on stack inside foo(). The list [1, 2, 3] is allocated on the heap. When function returned, x gets the pointer.
The list is NOT destroyed because the heap memory remains valid as long as x exists.

7. Objects Shared Between Scopes = Heap
Only heap allows objects to outlive the scope they were created in
"""
def outer():
    data = [1]

    def inner():
        print(data)

    return inner

closure = outer()
closure()
"""
Here:
    * data list is on heap
    * inner() accesses it later—after outer() has finished
    * So heap enables this shared lifespan

8. Heap and Memory Leaks
Because heap allocations are manual (via refcount + GC), memory leaks can happen if:
    * Reference cycles aren't collected
    * Native extensions allocate memory and forget to free
    * Long-lived objects hold large references
CPython GC uses generational GC to help—but not foolproof.
"""
