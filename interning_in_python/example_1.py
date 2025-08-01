# Consider this example in a text analysis tool:

from sys import intern, getrefcount

def tokenize(text):
    return [intern(word) for word in text.split()]

text1 = "yes no yes no yes no"
text2 = "no yes no yes no yes"

tokens1 = tokenize(text1)
tokens2 = tokenize(text2)

print(tokens1)
print(tokens2)

print(getrefcount(tokens1))
print(getrefcount(tokens2))

print(tokens1[0] is tokens2[1])

"""
-> Interning in CPython Source Code : Interned strings are stored in a global dictionary (called interned or similar).
When you call sys.intern(), it checks this dictionary first. If the string is already interned, it returns the reference. 
Otherwise, it adds the string to the dictionary.
"""