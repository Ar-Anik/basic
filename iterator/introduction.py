"""
Link : https://www.geeksforgeeks.org/python/iterators-in-python/

Q : What is an Iterator in Python?
-> An iterator is an object in Python that represents a stream of data. It returns one element at a time when we call
the built-in function next() on it.

# Iterator Implements Two Methods:
1. __iter__() — returns the iterator object itself.
2. __next__() — returns the next value from the iterator. Raises StopIteration when no more data.

"""

# Built-in Iterator from a List
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

"""
Q : What is Lazy Evaluation?
-> Lazy evaluation means Python delays computation or fetched of values until they are needed.
In the case of iterators:
    * Values are not pre-computed
    * Each value is computed (or fetched) only when next() is called
    * It saves memory and makes it possible to work with infinite sequences

# When we call next() on an iterator:
    * The internal pointer moves forward by one step
    * The iterator does not remember the value it just returned
    * we cannot go back to previous items
    * Iterators are forward-only
    * Designed for lazy evaluation
"""