import weakref

class User:
    def __init__(self, name):
        self.name = name

user_cache = weakref.WeakValueDictionary()
print(type(user_cache))

u = User("Anik")
user_cache["anik"] = u

"""
WeakValueDictionary stores weak references to values. So "anik" → weak reference to the User object.
WeakValueDictionary does NOT increase the reference count of the object. Now:
    * One strong reference: u
    * One weak reference: user_cache["anik"]
"""

print(user_cache.items())
print(user_cache["anik"].name)

del u
"""
Now there are no strong references to the User("Anik") object. Python's garbage collector immediately 
destroys the object. The weak reference inside user_cache is now pointing to a dead object.
"""

print(user_cache.get("anik"))
"""
Since the actual object is gone, the weak reference returns None. So user_cache["anik"] is automatically 
removed from the dictionary. This behavior prevents memory leaks — the dictionary does not hold onto 
dead objects.
"""
