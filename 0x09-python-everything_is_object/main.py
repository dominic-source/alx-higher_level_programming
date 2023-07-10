#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
print(lc.first_name)
print("--")

lc.first_name = "Doe"
print(lc.first_name)
print("--")

lc.first_name = "Jane"
lc.first_name = "Tunde"
print(lc.first_name)
print("--")

obj = LockedClass()
obj.first_name = "John"
del obj.first_name
print(hasattr(obj, "first_name"))
print("--")

obj = LockedClass()
obj.last_name = "Doe"
