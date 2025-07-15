"""
Link : https://www.geeksforgeeks.org/python/generators-in-python/

-> A generator function in Python is a special type of function that allows us to pause execution and return a value using
the yield keyword, resuming later from where it left off.

-> This makes it ideal for generating sequences of values on-the-fly and efficiently handling large data sets or streams
without storing them all in memory.

-> When we call a generator function, it doesn't run immediately. It returns a generator object, which is an iterator.
we can loop over it using a for loop or manually call next().

-> Every generator function follows the Iterator Protocol:
    * Has __iter__() that returns itself
    * Has __next__() to yield the next value
"""

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gtr = count_up_to(3)
print(gtr.__next__())
print(next(gtr))
print(gtr.__next__())
print(next(gtr))

"""
-> First call to next(gtr) or gtr.__next__() starts count_up_to() and runs until the first yield i.
-> Each next() resumes from where it left off.
-> When the function finishes(i = 4), a StopIteration is raised.
"""

"""
Q : Why Use Generators?
1. Memory Efficiency
We don’t load all values into memory. Perfect for:
    * Streaming large files (e.g., logs, CSVs)
    * Generating infinite sequences (e.g., Fibonacci, primes)

2. Lazy Evaluation
Values are computed on demand, not all at once.
"""
