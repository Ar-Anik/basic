"""
-> The call stack is a stack (LIFO – Last In, First Out) that stores information about active function calls, including
local variables and the return address.

-> Call stack a logical structure (within stack memory) that tracks active function calls. It is implemented using the
stack data structure. It stores stack frames, each representing one function call. Each frame contains:
    * Local variables
    * Arguments
    * Return address (where to go after function finishes)

> Think of stack memory as a big building.
> Each floor = memory space
> The call stack is like the elevator that tracks which floor (function call) i am on.
> When a function is called, i go up a floor (push a frame).
> When the function ends, i come down (pop the frame).
"""
def function_A():
    a = 5
    function_B()

def function_B():
    b = 10

function_A()
"""
> when function_A() call, create a stack frame and pushes frame onto the call stack in stack memory.
> again when function_B() call, create function_B stack frame and pushes its own frame.
> Both use stack memory to store their local variables.
> When done, frames are popped.
"""
def greet():
    name = "Anik"
    print("Hello", name)

def main():
    greet()

main()
"""
> Step-1: Program starts
    * Python runtime starts the program.
    * It implicitly calls the main() function.
    * So, the call stack pushes the main frame.
Stack DataStructure:  
    [ main() ]

> Step-2: Inside main(), it calls greet()
* Now greet() is called.
* A new frame is pushed onto the stack — LIFO: new on top
Stack DataStructure: 
    [ greet() ]
    [ main() ]
* Local variable name = "Anik" is stored inside the greet() frame.
* It prints Hello Anik.

> Step 3: greet() ends
    * Now the greet() function ends.
    * According to LIFO, the last pushed frame is the first to pop.
    * So we pop greet() off the stack.
    * Execution goes back to main().
Stack DataStructure: 
[ main() ]

Step 4: main() ends
    * Now main() function also finishes.
    * Again, LIFO principle: it's the next to be popped.
Stack DataStructure: 
(empty)
"""

"""
Python manages the call stack internally. we can see it during an exception trace:
"""
def fun_a():
    fun_b()

def fun_b():
    fun_c()

def fun_c():
    1/0

fun_a()

"""
Error output (truncated) : 
Traceback (most recent call last):
  File "/Users/aubdurrobanik/Desktop/basic/memory_allocation_in_python/stack_memory/call_stack.py", line 83, in <module>
    fun_a()
    ~~~~~^^
  File "/Users/aubdurrobanik/Desktop/basic/memory_allocation_in_python/stack_memory/call_stack.py", line 75, in fun_a
    fun_b()
    ~~~~~^^
  File "/Users/aubdurrobanik/Desktop/basic/memory_allocation_in_python/stack_memory/call_stack.py", line 78, in fun_b
    fun_c()
    ~~~~~^^
  File "/Users/aubdurrobanik/Desktop/basic/memory_allocation_in_python/stack_memory/call_stack.py", line 81, in fun_c
    1/0
    ~^~
ZeroDivisionError: division by zero

This is the call stack trace showing how the functions were called.
"""