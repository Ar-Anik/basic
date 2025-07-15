"""
Link : https://www.geeksforgeeks.org/python/python-yield-keyword/ (Advantages and Disadvantages)

-> The yield keyword in Python is like return, but instead of ending the function, it return value and pauses the function
and remembers where it left off.

-> It lets you generate values one by one (lazy evaluation), which is useful for looping through large datasets or infinite
sequences.

-> The yield keyword in Python is used in a function to turn it into a generator, which allows the function to return values
one at a time and pause its state between each return.

-> How it Works (Step-by-Step):
    * When Python sees yield in a function, it treats the function as a generator function.
    * Calling the function does not run it immediately. Instead, it returns a generator object.
    * When iterate over the generator (e.g., using for, next(), or in a loop), and the function runs up to the next yield.
    * The function pauses at yield and waits until the next iteration resumes it.
    * It resumes from exactly where it left off, keeping all variable states intact.
"""


import pdb
def count_up_to(n):
    print("Start Generator Function.")
    i = 1
    while i <= n:
        print(f"Yielding {i}")
        pdb.set_trace()
        print("->", f"Before yield {i}")
        yield i
        print("->", f"After yield {i}")
        pdb.set_trace()
        i += 1
        print(f"Incremented i to {i}")

gtr = count_up_to(3)
print(gtr.__dir__())
print("type of gtr : ", type(gtr))

"""
When a function uses the yield keyword, Python makes it a generator function, and calling it returns a generator object. 
This generator object implements both the __next__() and __iter__() methods.
"""

itr = iter(gtr)
print(itr.__dir__())
print("type of itr : ", type(itr))

while True:
    try:
        pdb.set_trace()
        val = next(itr)
        print("Value : ", val)
    except StopIteration:
        break


"""
# Case-1
    * When a function has yield, calling it (like count_up_to(3)) returns a generator object (gtr).
    * Generator objects automatically implement the iterator protocol, i.e., they have:
        1. __iter__() — returns self
        2. __next__() — gives next value or raises StopIteration

So when you write: itr = iter(gtr)
It’s the same object: iter(gtr) is gtr  # True
Because iter() method return object itself.

That means:
    * Both gtr and itr point to the same generator object.
    * Generator is itself an iterator.   
"""

"""
# Case-2
When first time call next(itr):
    * The generator function starts.
    * It runs up to the yield i line.
    * yield sends the value i to the next() caller.
    * Then the function pauses — it does not execute i += 1 until the next next() call.
    * When next() is called again, it resumes just after the previous yield, and executes i += 1, then loops back.
So:
    * yield both returns a value and pauses the function.
    * next() resumes from after the last yield, not before.
"""

"""
# Case-3
When i = 4, the while condition i <= n is False → the loop ends → generator raises StopIteration on the next next() call.

So,
    * When the generator function reaches the end of code (or returns normally without a yield), Python automatically 
      raises StopIteration.
    * The for loop or manual next() catches this and ends the iteration.
"""

