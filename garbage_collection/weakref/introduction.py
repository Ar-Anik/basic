"""
Q : What is weakref?
-> A weakref (weak reference) is a reference to an object that does not increase its reference count. When the object has
no strong references, it can still be automatically garbage collected, even if a weak reference to it still exists.
In simpler terms:
    * A normal (strong) reference keeps the object alive.
    * A weak reference does not keep the object alive — it's like pointing to something lightly, and if it disappears,
      our pointer goes dead.
It's like saying: “I know that object, but I’m not holding on to it.”

Q : Why use weakref?
    * Avoid memory leaks caused by circular references
    * Allow objects to be referenced without preventing GC
Common use cases:
    * Caches (e.g., WeakValueDictionary)
    * Object graphs
    * Observer patterns

"""

# Q : How to use weakref.ref()?
import weakref
import sys

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value : {self.value}"

obj = MyClass(10)           # it strong reference
print(sys.getrefcount(obj))

weak_obj = weakref.ref(obj)     # it weak reference
print(sys.getrefcount(obj))

"""
obj is a strong reference — keeps the object alive. weak_obj is a weak reference — does NOT increase reference count.
"""

# Q : How to use the weak reference?
print(obj)
print(weak_obj())     # Returns original object if still alive
print(weak_obj().__class__)     # Access attributes or methods via weakref()

# Q : What happens when strong reference is deleted ?
del obj
print(weak_obj())

"""
The object was garbage collected as soon as the last strong reference (obj) was deleted. Python reclaims the memory 
automatically. The weak reference does not protect the object. weak_obj() returns None because the original object 
is gone. we can't access any properties or methods after the object is gone from memory. 
"""

"""
-> Types of weak references in Python : 
    * weakref.ref(obj) : Simple weak reference
    * weakref.WeakValueDictionary : Dictionary where values are weak references
    * weakref.WeakKeyDictionary : Dictionary where keys are weak references
    * weakref.finalize(obj, func) : Call func when obj is about to be GC’d
"""

