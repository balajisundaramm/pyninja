"""
Text :  str
Numeric : int, float, complex
Sequence : list, tuple, range
Mapping : dict
Set : set, frozenset
Bool :  bool
Binary : bytes, bytearray, memoryview
None Type :  NoneType

type() will return the data type
"""

#str
x="Hello world"
print(x)
print(type(x))

#int
x=5
print(x)
print(type(x))

#float
x=20.5 #35e3
print(x)
print(type(x))

#complex
x=1j
print(x)
print(type(x))

#list
x=list(("apple", "banana", "cherry"))
print(x)
print(type(x))

#tuple
x=tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

#range
x=range(6)
print(x)
print(type(x))

#dict
x=dict(name="John", age=36) #{"name" : "John", "age" : 36}
print(x)
print(type(x))

#set
x=set(("apple", "banana", "cherry"))
print(x)
print(type(x))

#frozenset
x=frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

#bool
x=bool(5)
print(x)
print(type(x))

x=bytes(5)
print(x)
print(type(x))

x=bytearray(5)
print(x)
print(type(x))

x=memoryview(bytes(5))
print(x)
print(type(x))

#Random
import random

print(random.randrange(1, 10))
print(random.randint(0,10)) # generates random int
print(random.uniform(0, 10)) # generates random float