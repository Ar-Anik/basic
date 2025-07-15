"""
Q : What is a Generator Expression in Python?
-> A generator expression is a concise way to create generators without defining a separate generator function with
def and yield. It looks like a list comprehension, but uses round parentheses () instead of square brackets [].

-> Generator Expression vs List Comprehension
--------------------------------------------------------------------------------------------------------------
Feature	            List Comprehension	                    Generator Expression
--------------------------------------------------------------------------------------------------------------
Syntax	            [x * x for x in range(5)]	            (x * x for x in range(5))
-------------------------------------------------------------------------------------------------------------
Result	            A full list in memory	                A generator (lazy evaluation)
--------------------------------------------------------------------------------------------------------------
Evaluation	        Eager (creates entire list)	            Lazy (one item at a time)
--------------------------------------------------------------------------------------------------------------
Memory usage	    High for large sequences	            Low — uses no extra memory
--------------------------------------------------------------------------------------------------------------
Execution time	    Faster for small inputs	                Faster for large or infinite data
--------------------------------------------------------------------------------------------------------------
"""

"""
-> Syntax of Generator Expression
(expression for item in iterable if condition)

This is similar to a list comprehension but generates items on demand.
"""

squares_1 = (x * x for x in range(3))

print(squares_1.__dir__())
print(next(squares_1))
print(next(squares_1))
print(next(squares_1))
# print(next(squares_1))

# This creates a generator object that computes x * x for x from 0 to 4. Internally Python does something like this:
def squares_gen():
    for x in range(3):
        yield x * x

# even though you didn't write yield, Python builds a generator function behind the scenes.

squares_2 = squares_gen()
print(squares_2.__dir__())

print(squares_2.__next__())
print(next(squares_2))
print(next(squares_2))


"""
-> Limitations of Generator Expressions
    * Can only contain a single expression.
    * Not suitable for complex logic (e.g., multiple yield points or multiple for loops with complex state).
    * Not reusable: once a generator is exhausted, it can't be restarted.
If need complex behavior, use a generator function instead.
"""
