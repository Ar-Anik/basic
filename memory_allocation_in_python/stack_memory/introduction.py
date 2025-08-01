"""
--> Stack Memory
The stack memory is a reserved region in a process's virtual address space that grows downward (from higher to
lower memory addresses). Stack memory is a special region of memory that stores data related to active function
calls. Each time a function is called, a new stack frame is created and pushed onto the call stack. When the
function ends, that frame is popped off the stack.

> Stack Memory works on the LIFO (Last-In-First-Out) principle:
    * The most recently called function is the first to return.
    * Each function call gets its own stack frame.

-> Stack Location (in process memory layout)
Here is a simplified virtual memory layout of a process in a 64-bit Linux or Unix-like OS:

    High Address
    │
    │  +-------------------+
    │  |   Stack Memory    | ← grows downward (towards lower memory addresses)
    │  +-------------------+
    │  |      ...          |
    │  |  Heap Memory      | ← grows upward (used for dynamic allocation)
    │  +-------------------+
    │  |  BSS Segment       | (uninitialized global/static vars)
    │  +-------------------+
    │  |  Data Segment      | (initialized global/static vars)
    │  +-------------------+
    │  |  Text Segment      | (executable code)
    │  +-------------------+
    │
    Low Address

Q : Where Is the Stack Stored?
Physically: It's stored in RAM, like the rest of process memory.
Logically: It lives at the top of the process's virtual memory space.
In Linux, stack starts at a high address (like 0x7fff_ffff_ffff) and grows downward.

-> Stack Frame (Core Concept)
A stack frame is a section of stack memory allocated for one function call. Unlike C or C++, Python (specifically
CPython) does not use the CPU’s hardware stack directly. Instead, it manages its own virtual stack of frames in
memory using PyFrameObject. So, stack frame is a PyFrameObject. Stack Frame includes part :

1. Return Address : When a function is called, the CPU must remember where it came from so it can return after
the function finishes. So, it stores the address of the next instruction (right after the function call) in the
stack. In CPython Python’s virtual machine uses bytecode. Each function call creates a new PyFrameObject with
its own instruction pointer (f_lasti) that tells Python what instruction to execute next when the function returns.
"""

def add(a, b):
    return a + b

def do_math():
    result = add(10, 20)
    print("Result : ", result)

do_math()

"""
Internally in CPython:
> do_math() is called: 
    * A new PyFrameObject(Stack Frame) is created for do_math.
    * Its f_lasti starts at -1 (meaning no bytecode has run yet).
> CPython begins running the bytecode of do_math():
    * The bytecode for add(10, 20) is executed.
    * Before the CALL_FUNCTION bytecode: f_lasti points to the instruction before the call.
    * Just after the call is prepared, and before jumping to the add() frame, CPython saves the current instruction 
      index into do_math's frame (f_lasti).
    * A new frame is pushed for add().
> While add() runs:
    * It has its own PyFrameObject with its own f_lasti, globals, and locals.
> After add() returns:
    * CPython pops the add() frame.
    * Resumes execution of do_math() at the index saved in f_lasti.

2. Function Arguments (Values passed to the function)
These are the inputs to a function. They are stored in the function's stack frame as local variables.
"""
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
"""
Calling greet("Alice", 30): Arguments: name = "Anik" and age = 14. These are stored in greet()'s frame (in f_locals in CPython)
> CPython Internals:
    * Arguments are stored in f_localsplus[] array of the PyFrameObject
    * Named variables like name and age are mapped by index to this array
    * The function's code object (PyCodeObject) tells how many arguments it expects and their names

3. Local Variables (Temporary variables defined inside the function)
These are variables created and used only inside the function. They are private to the function and disappear when the function 
returns (i.e., when the stack frame is popped).
"""
def square(x):
    result = x * x   # ← local variable
    return result
"""
Here:
    * result is a local variable.
    * Stored in the stack frame of square()
> CPython Internals:
    * Local variables are stored in the same array as arguments: f_localsplus[]
    * Their names and offsets are recorded in the function's code object (co_varnames)

4. Function Metadata (Frame information, bytecode, links)
Each function call stores metadata that Python needs to:
    * Track where i am in the function
    * Link frames together for traceback
    * Store references to built-ins, globals, etc.

> Metadata Includes:
| Name         | Description                               |
| ------------ | ----------------------------------------- |
| f_lasti      | Index of the current bytecode instruction |
| f_back       | Link to the previous (caller) frame       |
| f_globals    | Global variables for the function         |
| f_builtins   | Built-in namespace (`len`, `print`, etc.) |
| f_code       | The `code object` describing the function |
| f_localsplus | Fast access to arguments + locals         |
|----------------------------------------------------------|
"""

import inspect

def debug_me(x):
    frame = inspect.currentframe()
    print("Function Name : ", frame.f_code.co_name)
    print("Caller Frame : ", frame.f_back.f_code.co_name)
    print("Argument x : ", frame.f_locals['x'])

def caller():
    debug_me(42)

caller()

"""
> Notes :
    * Stack memory is temporary: Each stack frame is discarded after the function returns.
    * Python uses the C stack via the PyFrameObject chain.
    * Deep recursion = stack overflow because each call adds a new frame.

> LIFO Behavior (Last In, First Out)
Functions use stack memory in LIFO order:
"""
def functin_a():
    functin_b()

def functin_b():
    functin_c()

def functin_c():
    print("In Function C")

# functin_a()

"""
Stack grows like:
[function_c()]   ← Top of stack
[function_b()]
[function_a()]   ← Bottom

function_c() is the last function called, but first to return. After function_c() finishes, it is popped off the stack, and control returns to function_b().
"""

"""
Stack Memory Managed By: CPU + compiler + OS.
"""
