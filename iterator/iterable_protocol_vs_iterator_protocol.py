"""
Q : What Is the Iterable Protocol?
-> The Iterable Protocol is a rule in Python that says, If we want our object to be usable in a for loop, it must have a
method called __iter__() that returns an iterator.

An object is an iterable if it implements the method: __iter__()

__iter__() must return an iterator object. That returned object must implement the Iterator Protocol.
"""

"""
Q : What is the Iterator Protocol?
-> The Iterator Protocol is a set of rules in Python that says, If an object wants to produce values one at a time 
(like in a loop), it must define two special methods:
        * __iter__() and
        * __next__().

An object is an iterator if it implements:
    * __iter__()  # Returns self
    * __next__()  # Returns next item or raises StopIteration
"""
