"""
Q : What is an Iterable in Python?
-> An iterable is any object in Python that:
    1. we can use a loop directly on an iterable.
    2. iterable can produce an iterator when passed to the built-in iter() function
    3. Has a special method: __iter__()
"""

# Examples of Iterables:
# All of these are iterable
my_list = [1, 2, 3]
my_tuple = (4, 5)
my_str = "abc"
my_dict = {'a': 1, 'b': 2}
my_set = {7, 8, 9}

"""
# You can use a for loop on them
for i in my_list:
    print(i)
"""


# When we do:
for x in my_list:
    print(x)

# Python actually does:
itr = my_list.__iter__()
print(type(itr))

while True:
    try:
        x = next(itr)
        print(x)
    except StopIteration:
        break

"""
-> Python’s for loop uses iterators instead of direct indexing because:
    * It allows looping over all types of iterables, not just sequences
    * It supports lazy evaluation (efficient memory usage)
    * It allows looping over infinite or dynamic data streams
    * It keeps the loop clean, consistent, and safe (no IndexError, no manual tracking)
    
Q : Why not just use my_list[0], my_list[1], my_list[2]...?
Because not all iterables support indexing. Examples that do NOT support indexing:
    * set
    * dict
    * generator
    * file object
    * custom iterable objects
All these are iterable but not subscriptable (obj[i] fails). If for loop used indexing internally, 
it would break on these.

-> Python’s for loop treats everything iterable in the same way. Whether it’s a list, a string, a generator, 
a file or our own custom object — if it has __iter__(), it works. This design makes Python powerful, consistent 
and extensible.
"""

# make iterable to iterator by iter() method
str_iter = iter(my_str)

print(str_iter.__next__())
print(str_iter.__next__())
print(str_iter.__next__())

"""
Q : How does an Iterable convert into an Iterator using iter()?
-> When we call iter(some_iterable):
    * Python checks if some_iterable has a method __iter__()
    * It calls __iter__() and returns the iterator object

That iterator object will now have the __next__() method, which is used to fetch values one by one.
"""

"""
Difference Between Iterable and Iterator in Python
------------------------------------------------------------------------------------------------------------------------------------------------
Feature	                Iterable	                                            Iterator
------------------------------------------------------------------------------------------------------------------------------------------------
Purpose	                Represents a collection that can be looped over	        Produces one item at a time from an iterable
------------------------------------------------------------------------------------------------------------------------------------------------
Required Methods	    Must implement __iter__()	                            Must implement both __iter__() and __next__()
------------------------------------------------------------------------------------------------------------------------------------------------
Usage	                Used as input to iter() to get an iterator	            Used with next() to fetch items one by one
------------------------------------------------------------------------------------------------------------------------------------------------
Loop Behavior	        Creates a new iterator each time a loop starts	        Drives the loop by yielding the next value in sequence
------------------------------------------------------------------------------------------------------------------------------------------------
Reusability	            Can be reused to start multiple loops	                Can be used only once unless recreated or reset
------------------------------------------------------------------------------------------------------------------------------------------------
Examples	            List, Tuple, String, Set, Dictionary	                Iterator returned by iter(list), file objects, generators
------------------------------------------------------------------------------------------------------------------------------------------------
"""

# What does Python actually do internally when we write a for loop with a range() and indexing like this?
lst = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(3, 6):
    print(lst[i])

"""
This loop has two parts:
    * range(3, 6) — this is an iterable that generates values: 3, 4, 5
    * Each value i is used to access lst[i]
So Python:
    * Turns range(3, 6) into an iterator
    * Iterates through values 3, 4, 5
    * In each iteration, it evaluates lst[i]
"""

# actually happen
itr = iter(range(3, 6))

while True:
    try:
        i = next(itr)
        print(lst[i])
    except StopIteration:
        break

"""
* range(3, 6) creates a range object: [3, 4, 5]
* iter(range(3, 6)) returns a range_iterator
* Python uses next() to get each index i
* lst[i] is accessed and printed

Here, lst is indeed an iterable, but also:
    * A sequence (like list, tuple, str)
    * Which supports random access using []
    * So lst[i] uses the __getitem__() method — not __iter__() or next()
    Example : print(lst[3]) --> lst.__getitem__(3)  # returns 'd'
"""


# What does Python actually do internally when we write a for loop with a dictionary.items() like this?
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key, val in dct.items():
    print(key, val)

dict_items = dct.items()
print(dict_items)
print(type(dict_items))
print(dict_items.__dir__())

"""
* dct.items() returns a dict_items object — a view, not an iterator
* It doesn't have a __next__() method
* But it does have __iter__() → which makes it an iterable
"""

# Python internally does this:
iterator = iter(dct.items())

while True:
    try:
        key, val = next(iterator)  # next() → gives us a tuple like ('a', 1), ('b', 2), etc.
        print(key, val)
    except StopIteration:
        break
