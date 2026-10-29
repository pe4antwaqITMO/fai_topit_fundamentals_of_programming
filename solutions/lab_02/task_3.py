import sys
import weakref

data = [1, 2, 3]
print(sys.getrefcount(data))

alias = data
print(sys.getrefcount(data))

container = [data]
print(sys.getrefcount(data))

del alias
print(sys.getrefcount(data))

container.clear()
print(sys.getrefcount(data))


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

# Практическая задача со словарем
registry = weakref.WeakValueDictionary()
r1 = Record()
r2 = Record()
r3 = Record()

registry['rec1'] = r1
registry['rec2'] = r2
registry['rec3'] = r3

print(list(registry.keys()))

del r3
print(list(registry.keys()))

del r2
print(list(registry.keys()))
