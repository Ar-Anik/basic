"""
Link : https://www.geeksforgeeks.org/python/memory-management-in-python/

Q : What Is Memory Management?
Memory management in Python refers to how the interpreter:
    * Allocates memory for variables, objects, functions
    * Keeps track of which objects are in use
    * Frees memory that’s no longer needed
"""

def function_a():
    name = "anik"
    print("Name :", name)

x = 1
y = 2
print(x + y)
function_a()

"""
Memory Allocation : 
Step-1: Python Interpreter Starts
    * Python process launches.
    * OS Allocator (malloc or mmap) allocates large chunks of raw memory from the operating system for the Python runtime to use.
    * Python Raw Allocator (PyMem_RawMalloc) wraps this, managing low-level raw allocations before higher-level allocators are ready.

Before anything else, CPython calls PyMem_RawMalloc() (a thin wrapper over malloc()) to bootstrap its own interpreter structures (import 
machinery, GC tables, internal caches). Underneath, PyMem_RawMalloc() uses the OS’s malloc() (or mmap()) to grab large blocks of heap space.

Step 2: Python Compiles Our Code to Bytecode
Our source code is parsed and compiled. As Python parses our .py, it creates code objects (PyCodeObject) for the module and for function_a.
Each code object (which holds bytecode, constant pool, variable names) is a small heap object allocated via PyObject_Malloc().
Function `function_a` code object (PyCodeObject), containing:
    * Bytecode instructions
    * Constants like string "anik"
    * Variable names, etc.

> Allocation:
    * The Object Allocator (PyObject_Malloc) allocates memory for the code object and constants.
    * It uses Arena Allocator to get memory pools from arenas.
    * If no pools available, Arena Allocator requests new arenas (256 KB chunks) from OS Allocator.

Step 3: Assignments: x = 1 and y = 2
    * Python creates integer objects for 1 and 2.
    * Small integers between -5 and 256 are pre-allocated (interned), so these already exist.
    * References x and y point to these pre-existing int objects (no new allocation needed here).

Step 4: Execute print(x + y)
    * Python computes x + y → creates int object 3 if not interned.
    * The Object Allocator allocates memory for this integer object if needed.
    * This allocation occurs from:
            A pool for small objects → from an arena → which is memory provided by OS Allocator.
    * Then Python calls print(), which creates its own stack frame (stack memory managed by CPU and interpreter, not in these allocators).
    
Step 5: Function Call function_a()
Interpreter creates a stack frame for function_a. Inside function_a():
    * The string "anik" constant is referenced (already stored in the code object at compile time).
    * A new reference to "anik" is placed in the local variable name.
    * The print function is called with this string.

> Memory Allocation Details:
    * Object Allocator manages the memory for the string "anik" object if not yet created.
    * The string lives in heap memory allocated from pools within arenas.
    * If pools are exhausted, Arena Allocator requests new arenas from OS Allocator.
    * The function's stack frame is handled by CPU/interpreter stack memory, separate from these heap allocators.
"""