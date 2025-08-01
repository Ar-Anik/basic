"""
Closures Function Link : https://www.geeksforgeeks.org/python/python-closures/

Q : What is Enclosing in Python?
-> In the context of functions, "enclosing" means that a function is wrapped inside another function — and the outer
function is said to be the enclosing function.
"""
def outer():        	# <--- Enclosing function
    x = 10           	# <--- Variable in enclosing scope
    def inner():     	# <--- Enclosed (inner) function
        print(x)     	# <--- Accessing variable from enclosing scope
    return inner
"""
Here, 
	* outer() is the enclosing function.
	* inner() is defined inside outer(), so it's enclosed by outer().
	* The variable x is in the enclosing scope of inner().

> Enclosing function : A function that contains another (nested) function inside it.
> Enclosed function : A function defined inside another function.
> Enclosing scope : The variable space of the enclosing function.

Q : What is Lexical Scope?
-> Lexical scope (also called static scope) means that Python decides variable scope based on where functions and 
variables are written in the code — not where they are called at runtime.
"""
def outer():
    msg = "Hello"
    def inner():
        print(msg)
    inner()

outer()
"""
msg is defined lexically (physically) inside outer(). inner() sees msg because of the lexical (text-based) location, 
not because it was called from outer().


Q : What is closures in python?
-> A closure in Python is a function that remembers the variables from the place where it was created, even after 
that place (outer function) is gone. Above example inner() is a closure function.

-> In Python, a closure is a function object that remembers values from its enclosing lexical scope, even if the 
outer function has finished executing.

A closure occurs when:
    * We have a nested function (a function defined inside another function),
    * The inner function references variables from the outer function, and
    * The outer function returns the inner function.
"""
def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    return inner_function

my_func = outer_function("Aubdur Rob Anik")
my_func()
"""
Even though outer_function has finished running, inner_function still has access to msg — that's a closure.

Q : Why closures are useful ?
> Encapsulation: You can hide data inside the closure.
> Function factories: They help in building customizable functions.
> State retention: Closures keep the state between calls without using global variables or classes.

Q : If the outer function no longer exists (i.e., has finished execution and its stack frame is gone), how can the inner function still be callable ?
-> Because : 
    * inner() was returned as a function object from outer().
    * Function objects are stored on the heap, not in the stack frame of the outer function.
    * The function object is alive as long as something (like variable f) holds a reference to it.
"""

# Example Function Factory :
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(10))

"""
Here, double and triple are closures that remember x as 2 and 3 respectively.
"""

"""
Q : If the stack frame is destroyed when a function returns, how does a Python closure remember variables from the outer (enclosing) function ?
-> When an inner function closes over (captures) a variable from an outer function, Python does NOT store that variable 
on the stack. Instead:
Python lifts that variable out of the stack frame and puts it in a heap-allocated object called a cell. That cell is 
then attached to the inner function via its __closure__.
"""
def outer():
    x = 10
    y = 20
    def inner():
        print(x)
    return inner

f = outer()

print(f.__closure__)        # Tuple of cell objects
print(f.__closure__[0].cell_contents)
"""
f.__closure__ → tuple of cell objects that hold the captured variables. Each cell contains a reference to the actual 
variable (x in this case), which lives on the heap, not the stack.

> In outer():
    * A stack frame is created.
    * Variable x = 10 is local in that frame.
    * inner() uses x from outer scope → Python detects this during compilation and marks x as a free variable for inner.

> So Python does:
    * Box `x` into a cell — a heap-allocated container.
    * inner gets a reference to that cell.
    * When outer() finishes, the stack frame is destroyed...
    * But the cell is still alive on the heap because inner holds a reference to it!
"""

